#!/usr/bin/env python3
"""
Digital Brain CADE - Graph Builder
====================================

Creates an interactive HTML graph visualization from extracted triples.
Uses D3.js force-directed graph for visualization.

Input: ~/brain_cade/graph/triples.json, entities.json
Output: ~/brain_cade/graph/brain_cade.html
"""
import json
from pathlib import Path
from collections import defaultdict

GRAPH_DIR = Path("~/brain_cade/graph/").expanduser()

# Color scheme for entity types
TYPE_COLORS = {
    "Nota Técnica": "#e74c3c",
    "Empresa": "#3498db",
    "Mercado": "#2ecc71",
    "Metodologia": "#f39c12",
    "Autor": "#9b59b6",
    "Processo": "#1abc9c",
    "Ano": "#95a5a6",
}

# Predicate styling
PREDICATE_COLORS = {
    "requerente_em": "#3498db",
    "atua_em": "#2ecc71",
    "analisa_mercado": "#27ae60",
    "utiliza_metodologia": "#f39c12",
    "autor_de": "#9b59b6",
    "processo": "#1abc9c",
    "departamento": "#e67e22",
    "ano": "#95a5a6",
    "tipo": "#e74c3c",
}


def build_graph():
    # Load data
    with open(GRAPH_DIR / "triples.json", encoding="utf-8") as f:
        triples = json.load(f)

    with open(GRAPH_DIR / "entities.json", encoding="utf-8") as f:
        entities = json.load(f)

    with open(GRAPH_DIR / "documents.json", encoding="utf-8") as f:
        documents = json.load(f)

    # Build nodes with size based on connectivity
    node_connections = defaultdict(int)
    for t in triples:
        node_connections[t["subject"]] += 1
        node_connections[t["object"]] += 1

    nodes = []
    for name, info in entities.items():
        connections = node_connections.get(name, 0)
        node_type = info["type"]
        nodes.append({
            "id": name,
            "type": node_type,
            "color": TYPE_COLORS.get(node_type, "#7f8c8d"),
            "size": min(5 + connections * 2, 40),
            "connections": connections,
            "source": info.get("source", ""),
        })

    # Build links
    links = []
    for t in triples:
        links.append({
            "source": t["subject"],
            "target": t["object"],
            "predicate": t["predicate"],
            "color": PREDICATE_COLORS.get(t["predicate"], "#bdc3c7"),
        })

    # Stats
    type_counts = defaultdict(int)
    for n in nodes:
        type_counts[n["type"]] += 1

    # Generate HTML
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Digital Brain CADE - Grafo de Conhecimento</title>
<script src="https://d3js.org/d3.v7.min.js"></script>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    background: #0a0a1a;
    color: #e0e0e0;
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
    overflow: hidden;
  }}
  #header {{
    position: absolute; top: 0; left: 0; right: 0;
    padding: 12px 20px;
    background: linear-gradient(180deg, rgba(10,10,26,0.95) 0%, rgba(10,10,26,0.7) 100%);
    z-index: 100;
    display: flex; align-items: center; gap: 20px;
    border-bottom: 1px solid rgba(255,255,255,0.05);
  }}
  #header h1 {{
    font-size: 18px; font-weight: 600;
    background: linear-gradient(135deg, #e74c3c 0%, #3498db 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  }}
  .stats {{
    font-size: 12px; color: #888;
    display: flex; gap: 15px;
  }}
  .stats span {{ color: #aaa; }}
  #legend {{
    position: absolute; bottom: 20px; left: 20px;
    background: rgba(10,10,26,0.9);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 8px; padding: 12px 16px;
    z-index: 100;
  }}
  #legend h3 {{ font-size: 12px; margin-bottom: 8px; color: #666; text-transform: uppercase; letter-spacing: 1px; }}
  .legend-item {{ display: flex; align-items: center; gap: 8px; margin: 4px 0; font-size: 12px; }}
  .legend-dot {{ width: 10px; height: 10px; border-radius: 50%; }}
  #controls {{
    position: absolute; top: 60px; right: 20px;
    background: rgba(10,10,26,0.9);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 8px; padding: 12px;
    z-index: 100;
  }}
  #controls label {{ font-size: 11px; color: #888; display: block; margin-top: 8px; }}
  #controls input[type="text"] {{
    background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1);
    color: #e0e0e0; padding: 6px 10px; border-radius: 4px; width: 200px;
    font-size: 12px; margin-top: 4px;
  }}
  #controls input[type="range"] {{ width: 180px; }}
  #tooltip {{
    position: absolute; display: none;
    background: rgba(15,15,35,0.95);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 6px; padding: 10px 14px;
    font-size: 12px; max-width: 350px;
    pointer-events: none; z-index: 200;
  }}
  #tooltip .tt-name {{ font-weight: 600; font-size: 14px; margin-bottom: 4px; }}
  #tooltip .tt-type {{ color: #888; font-size: 11px; }}
  #tooltip .tt-connections {{ color: #aaa; margin-top: 4px; }}
  #tooltip .tt-relations {{ margin-top: 6px; font-size: 11px; line-height: 1.4; }}
  .link {{ stroke-opacity: 0.15; }}
  .link.highlighted {{ stroke-opacity: 0.8; stroke-width: 2px; }}
  .node {{ cursor: pointer; stroke-width: 1; stroke: rgba(255,255,255,0.2); }}
  .node:hover {{ stroke: white; stroke-width: 2; }}
  .node.dimmed {{ opacity: 0.1; }}
  .link.dimmed {{ stroke-opacity: 0.03; }}
  #info-panel {{
    position: absolute; bottom: 20px; right: 20px;
    width: 300px; max-height: 400px; overflow-y: auto;
    background: rgba(10,10,26,0.95);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 8px; padding: 16px; z-index: 100;
    display: none;
  }}
  #info-panel h3 {{ font-size: 14px; color: #e74c3c; margin-bottom: 8px; }}
  #info-panel .info-row {{ font-size: 12px; margin: 4px 0; }}
  #info-panel .info-label {{ color: #888; }}
</style>
</head>
<body>
<div id="header">
  <h1>🧠 Digital Brain CADE</h1>
  <div class="stats">
    <span>{len(nodes)} entidades</span>
    <span>{len(links)} relações</span>
    <span>{len(documents)} documentos</span>
  </div>
</div>

<div id="controls">
  <label>Buscar nó</label>
  <input type="text" id="search" placeholder="Empresa, mercado, nota...">
  <label>Tipo de filtro</label>
  <select id="type-filter" style="background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);color:#e0e0e0;padding:6px;border-radius:4px;width:200px;font-size:12px;">
    <option value="all">Todos</option>
    {''.join(f'<option value="{t}">{t} ({c})</option>' for t, c in sorted(type_counts.items()))}
  </select>
  <label>Força do grafo: <span id="force-val">0.3</span></label>
  <input type="range" id="force-slider" min="0.05" max="1" step="0.05" value="0.3">
</div>

<div id="legend">
  <h3>Entidades</h3>
  {''.join(f'<div class="legend-item"><div class="legend-dot" style="background:{c}"></div>{t} ({type_counts.get(t,0)})</div>' for t, c in TYPE_COLORS.items() if type_counts.get(t,0) > 0)}
</div>

<div id="tooltip"></div>

<div id="info-panel">
  <h3 id="panel-title"></h3>
  <div id="panel-content"></div>
</div>

<svg id="graph" width="100%" height="100%"></svg>

<script>
const nodes = {json.dumps(nodes, ensure_ascii=False)};
const links = {json.dumps(links, ensure_ascii=False)};
const documents = {json.dumps(documents, ensure_ascii=False)};

// Build adjacency for quick lookups
const adj = {{}};
links.forEach(l => {{
  if (!adj[l.source]) adj[l.source] = [];
  if (!adj[l.target]) adj[l.target] = [];
  adj[l.source].push(l);
  adj[l.target].push(l);
}});

const width = window.innerWidth;
const height = window.innerHeight;

const svg = d3.select("#graph")
  .attr("width", width)
  .attr("height", height);

// Zoom
const zoom = d3.zoom()
  .scaleExtent([0.1, 8])
  .on("zoom", (event) => g.attr("transform", event.transform));
svg.call(zoom);

const g = svg.append("g");

// Simulation
const simulation = d3.forceSimulation(nodes)
  .force("link", d3.forceLink(links).id(d => d.id).distance(60))
  .force("charge", d3.forceManyBody().strength(-120))
  .force("center", d3.forceCenter(width / 2, height / 2))
  .force("collision", d3.forceCollide().radius(d => d.size / 2 + 3));

const link = g.append("g")
  .selectAll("line")
  .data(links)
  .join("line")
  .attr("class", "link")
  .attr("stroke", d => d.color)
  .attr("stroke-width", 1);

const node = g.append("g")
  .selectAll("circle")
  .data(nodes)
  .join("circle")
  .attr("class", "node")
  .attr("r", d => d.size / 2)
  .attr("fill", d => d.color)
  .call(d3.drag()
    .on("start", dragstarted)
    .on("drag", dragged)
    .on("end", dragended));

// Labels for important nodes
const label = g.append("g")
  .selectAll("text")
  .data(nodes.filter(n => n.size > 10))
  .join("text")
  .text(d => d.id.length > 25 ? d.id.substring(0, 22) + "..." : d.id)
  .attr("font-size", "9px")
  .attr("fill", "#ccc")
  .attr("dx", d => d.size / 2 + 4)
  .attr("dy", 3);

// Tooltip
const tooltip = document.getElementById("tooltip");

node.on("mouseover", function(event, d) {{
  tooltip.style.display = "block";
  tooltip.innerHTML = `
    <div class="tt-name">${{d.id}}</div>
    <div class="tt-type">${{d.type}}</div>
    <div class="tt-connections">${{d.connections}} conexão(ões)</div>
    <div class="tt-relations">${{(adj[d.id]||[]).slice(0,5).map(l => 
      l.source.id === d.id 
        ? `→ ${{l.predicate}} → ${{l.target.id}}`
        : `← ${{l.predicate}} ← ${{l.source.id}}`
    ).join('<br>')}}</div>`;
}}).on("mousemove", function(event) {{
  tooltip.style.left = (event.pageX + 15) + "px";
  tooltip.style.top = (event.pageY - 10) + "px";
}}).on("mouseout", function() {{
  tooltip.style.display = "none";
}});

// Click to show info panel
node.on("click", function(event, d) {{
  showInfoPanel(d);
}});

function showInfoPanel(d) {{
  const panel = document.getElementById("info-panel");
  const title = document.getElementById("panel-title");
  const content = document.getElementById("panel-content");
  
  title.textContent = d.id;
  
  let html = `<div class="info-row"><span class="info-label">Tipo:</span> ${{d.type}}</div>`;
  
  const relations = adj[d.id] || [];
  const subjects = [...new Set(relations.filter(l => l.target.id === d.id).map(l => l.source.id))];
  const objects = [...new Set(relations.filter(l => l.source.id === d.id).map(l => l.target.id))];
  
  if (subjects.length) html += `<div class="info-row"><span class="info-label">Referenciado por:</span> ${{subjects.slice(0,10).join(", ")}}</div>`;
  if (objects.length) html += `<div class="info-row"><span class="info-label">Referencia:</span> ${{objects.slice(0,10).join(", ")}}</div>`;
  
  // If it's a Nota Técnica, show document details
  if (d.type === "Nota Técnica") {{
    const doc = documents.find(doc => `NT_${{doc.nota_number}}_${{doc.nota_year}}` === d.id);
    if (doc) {{
      if (doc.process_number) html += `<div class="info-row"><span class="info-label">Processo:</span> ${{doc.process_number}}</div>`;
      if (doc.requerentes && doc.requerentes.length) html += `<div class="info-row"><span class="info-label">Requerentes:</span> ${{doc.requerentes.join(", ")}}</div>`;
      if (doc.ementa) html += `<div class="info-row" style="margin-top:8px">${{doc.ementa.substring(0, 300)}}...</div>`;
    }}
  }}
  
  content.innerHTML = html;
  panel.style.display = "block";
}})

// Search
document.getElementById("search").addEventListener("input", function(e) {{
  const query = e.target.value.toLowerCase();
  if (!query) {{
    node.classed("dimmed", false);
    link.classed("dimmed", false);
    label.attr("opacity", 1);
    return;
  }}
  const matches = new Set(nodes.filter(n => n.id.toLowerCase().includes(query)).map(n => n.id));
  node.classed("dimmed", d => !matches.has(d.id));
  link.classed("dimmed", d => !matches.has(d.source.id) && !matches.has(d.target.id));
  label.attr("opacity", d => matches.has(d.id) ? 1 : 0.2);
}});

// Type filter
document.getElementById("type-filter").addEventListener("change", function(e) {{
  const type = e.target.value;
  if (type === "all") {{
    node.classed("dimmed", false);
    link.classed("dimmed", false);
    label.attr("opacity", 1);
    return;
  }}
  const typeMatches = new Set(nodes.filter(n => n.type === type).map(n => n.id));
  node.classed("dimmed", d => !typeMatches.has(d.id));
  link.classed("dimmed", d => !typeMatches.has(d.source.id) && !typeMatches.has(d.target.id));
  label.attr("opacity", d => typeMatches.has(d.id) ? 1 : 0.2);
}});

// Force slider
document.getElementById("force-slider").addEventListener("input", function(e) {{
  const val = parseFloat(e.target.value);
  document.getElementById("force-val").textContent = val;
  simulation.force("charge").strength(-120 * val);
  simulation.alpha(0.3).restart();
}});

// Drag
function dragstarted(event) {{ if (!event.active) simulation.alphaTarget(0.3).restart(); event.subject.fx = event.subject.x; event.subject.fy = event.subject.y; }}
function dragged(event) {{ event.subject.fx = event.x; event.subject.fy = event.y; }}
function dragended(event) {{ if (!event.active) simulation.alphaTarget(0); event.subject.fx = null; event.subject.fy = null; }}

// Click SVG background to close panel
svg.on("click", function(e) {{
  if (e.target.tagName === "svg") {{
    document.getElementById("info-panel").style.display = "none";
  }}
}});
</script>
</body>
</html>"""

    output_path = GRAPH_DIR / "brain_cade.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ Graph visualization saved to: {output_path}")
    print(f"   Open in browser: file://{output_path}")
    print(f"   Nodes: {len(nodes)}, Links: {len(links)}")

if __name__ == "__main__":
    build_graph()