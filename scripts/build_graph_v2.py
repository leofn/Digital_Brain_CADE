#!/usr/bin/env python3
"""
Digital Brain CADE - Interactive Graph Builder v2
===================================================

Creates a beautiful interactive HTML network graph from extracted triples.
Features:
- Force-directed layout with D3.js
- Color-coded nodes by type
- Click to see connections
- Search/filter by entity type
- Zoom & pan
"""
import json
from pathlib import Path
from collections import Counter, defaultdict

GRAPH_DIR = Path("~/brain_cade/graph/").expanduser()
OUTPUT_DIR = Path("~/brain_cade/graph/").expanduser()

# Color palette for entity types
TYPE_COLORS = {
    "Empresa": "#4CAF50",        # Green
    "Mercado": "#FF9800",        # Orange
    "Nota Técnica": "#2196F3",   # Blue
    "Processo": "#9C27B0",       # Purple
    "Autor": "#F44336",          # Red
    "Metodologia": "#00BCD4",    # Cyan
    "Tipo de Operação": "#FFEB3B",  # Yellow
    "Ano": "#795548",            # Brown
}

# Predicate colors for edges
PREDICATE_COLORS = {
    "analisa": "#2196F3",
    "mercado_relevante": "#FF9800",
    "processo": "#9C27B0",
    "ano": "#795548",
    "autor_de": "#F44336",
    "aplica_metodologia": "#00BCD4",
    "tipo_operacao": "#FFEB3B",
    "adquire": "#4CAF50",
    "adquirida_por": "#8BC34A",
}

def load_data():
    with open(GRAPH_DIR / "entities.json", encoding="utf-8") as f:
        entities = json.load(f)
    with open(GRAPH_DIR / "triples.json", encoding="utf-8") as f:
        triples = json.load(f)
    return entities, triples

def build_graph_data(entities, triples):
    """Build D3.js-compatible graph data."""
    # Calculate node importance (connections)
    connections = Counter()
    for t in triples:
        connections[t["subject"]] += 1
        connections[t["object"]] += 1
    
    # Build nodes
    nodes = []
    node_ids = set()
    for name, info in entities.items():
        conns = connections.get(name, 0)
        if conns == 0 and info["type"] not in ("Nota Técnica",):
            continue  # Skip disconnected non-doc entities
        node = {
            "id": name,
            "type": info.get("type", "unknown"),
            "connections": conns,
            "aliases": info.get("aliases", []),
            "source": info.get("source", ""),
        }
        nodes.append(node)
        node_ids.add(name)
    
    # Add missing nodes referenced in triples
    for t in triples:
        for side in ["subject", "object"]:
            if t[side] not in node_ids:
                nodes.append({
                    "id": t[side],
                    "type": "unknown",
                    "connections": connections.get(t[side], 0),
                    "aliases": [],
                    "source": "",
                })
                node_ids.add(t[side])
    
    # Build links
    links = []
    for t in triples:
        if t["subject"] in node_ids and t["object"] in node_ids:
            links.append({
                "source": t["subject"],
                "target": t["object"],
                "predicate": t["predicate"],
            })
    
    return nodes, links

def generate_html(nodes, links, entities):
    """Generate the interactive HTML file."""
    # Type statistics
    type_counts = Counter(n["type"] for n in nodes)
    type_stats = ", ".join(f"{t}: {c}" for t, c in type_counts.most_common())
    
    # Predicate statistics
    pred_counts = Counter(l["predicate"] for l in links)
    pred_stats = ", ".join(f"{p}: {c}" for p, c in pred_counts.most_common(10))
    
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Digital Brain CADE - Grafo de Conhecimento</title>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ 
    background: #0d1117; 
    color: #c9d1d9; 
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
    overflow: hidden;
}}
#container {{ display: flex; height: 100vh; }}
#sidebar {{
    width: 340px; 
    background: #161b22; 
    border-right: 1px solid #30363d;
    overflow-y: auto; 
    padding: 20px;
    display: flex; flex-direction: column;
}}
#graph {{ flex: 1; position: relative; }}
svg {{ width: 100%; height: 100%; }}
h1 {{ 
    color: #58a6ff; font-size: 18px; margin-bottom: 4px;
    border-bottom: 1px solid #30363d; padding-bottom: 12px;
    letter-spacing: -0.5px;
}}
h1 .emoji {{ font-size: 22px; }}
.subtitle {{ color: #8b949e; font-size: 12px; margin-bottom: 16px; }}
.stats {{ 
    background: #21262d; border-radius: 8px; padding: 12px; 
    margin-bottom: 16px; font-size: 12px; 
}}
.stats strong {{ color: #58a6ff; }}
.control-group {{ margin-bottom: 16px; }}
.control-group label {{ 
    display: block; font-size: 12px; color: #8b949e; 
    margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.5px;
}}
.control-group input, .control-group select {{
    width: 100%; padding: 8px 12px; background: #0d1117; 
    border: 1px solid #30363d; border-radius: 6px; color: #c9d1d9;
    font-size: 14px; outline: none;
}}
.control-group input:focus, .control-group select:focus {{
    border-color: #58a6ff;
}}
.type-filter {{ display: flex; flex-wrap: wrap; gap: 6px; }}
.type-btn {{
    padding: 4px 10px; border-radius: 12px; font-size: 11px;
    cursor: pointer; border: 1px solid #30363d; background: #21262d;
    color: #c9d1d9; transition: all 0.2s;
}}
.type-btn.active {{ border-color: currentColor; }}
.type-btn:hover {{ background: #30363d; }}
#node-info {{
    margin-top: auto; background: #21262d; border-radius: 8px;
    padding: 12px; min-height: 100px;
}}
#node-info h3 {{ color: #58a6ff; font-size: 14px; margin-bottom: 8px; }}
#node-info .meta {{ font-size: 12px; color: #8b949e; }}
#node-info .connections {{ margin-top: 8px; }}
#node-info .conn-item {{ 
    padding: 3px 0; font-size: 12px; 
    border-bottom: 1px solid #30363d;
}}
#node-info .conn-item:last-child {{ border-bottom: none; }}
#node-info .conn-arrow {{ color: #58a6ff; margin: 0 6px; }}
#node-info .conn-type {{ 
    font-size: 10px; padding: 1px 5px; border-radius: 8px;
    background: #30363d; margin-left: 4px;
}}
.legend {{ margin-top: 12px; }}
.legend-item {{ 
    display: flex; align-items: center; gap: 8px; 
    font-size: 12px; padding: 2px 0;
}}
.legend-dot {{ 
    width: 10px; height: 10px; border-radius: 50%;
    display: inline-block; flex-shrink: 0;
}}
.tooltip {{
    position: absolute; background: #21262d; border: 1px solid #30363d;
    border-radius: 8px; padding: 8px 12px; font-size: 12px;
    pointer-events: none; z-index: 100; display: none;
    max-width: 300px;
}}
.tooltip .tt-name {{ color: #58a6ff; font-weight: 600; }}
.tooltip .tt-type {{ color: #8b949e; font-size: 11px; }}
</style>
</head>
<body>
<div id="container">
<div id="sidebar">
    <h1><span class="emoji">🧠</span> Digital Brain CADE</h1>
    <p class="subtitle">Grafo de Conhecimento — Notas Técnicas</p>
    
    <div class="stats">
        <strong>{len(nodes)}</strong> entidades · <strong>{len(links)}</strong> relações<br>
        <span style="font-size:11px; color:#8b949e;">{type_stats}</span>
    </div>
    
    <div class="control-group">
        <label>🔍 Buscar entidade</label>
        <input type="text" id="search" placeholder="Ex: Ipiranga, NT_07_2017...">
    </div>
    
    <div class="control-group">
        <label>Filtrar por tipo</label>
        <div class="type-filter" id="type-filters"></div>
    </div>
    
    <div class="control-group">
        <label>Relações mais comuns</label>
        <div class="stats" style="font-size:11px;">
            {pred_stats}
        </div>
    </div>

    <div class="legend" id="legend"></div>
    
    <div id="node-info">
        <h3>Clique em um nó para ver detalhes</h3>
        <div class="meta">Selecione uma entidade no grafo</div>
    </div>
</div>

<div id="graph">
    <svg id="svg"></svg>
</div>
</div>

<div class="tooltip" id="tooltip">
    <div class="tt-name" id="tt-name"></div>
    <div class="tt-type" id="tt-type"></div>
</div>

<script src="https://d3js.org/d3.v7.min.js"></script>
<script>
// Data
const nodes = {json.dumps(nodes, ensure_ascii=False)};
const links = {json.dumps(links, ensure_ascii=False)};
const typeColors = {json.dumps(TYPE_COLORS)};

// State
let activeTypes = new Set(Object.keys(typeColors));
let selectedNode = null;
let searchTerm = "";

// Setup SVG
const width = document.getElementById('graph').clientWidth;
const height = document.getElementById('graph').clientHeight;
const svg = d3.select('#svg').attr('viewBox', [0, 0, width, height]);

// Add zoom
const zoom = d3.zoom().scaleExtent([0.1, 8]).on('zoom', (event) => {{
    g.attr('transform', event.transform);
}});
svg.call(zoom);

const g = svg.append('g');

// Arrow marker
svg.append('defs').append('marker')
    .attr('id', 'arrowhead')
    .attr('viewBox', '-0 -5 10 10')
    .attr('refX', 18).attr('refY', 0)
    .attr('orient', 'auto')
    .attr('markerWidth', 6).attr('markerHeight', 6)
    .append('path').attr('d', 'M 0,-5 L 10,0 L 0,5').attr('fill', '#30363d');

// Build type filters
const types = [...new Set(nodes.map(n => n.type))];
const filterDiv = document.getElementById('type-filters');
types.forEach(t => {{
    const btn = document.createElement('button');
    btn.className = 'type-btn active';
    btn.style.color = typeColors[t] || '#8b949e';
    btn.style.borderColor = typeColors[t] || '#30363d';
    btn.textContent = `${{t}} (${{nodes.filter(n=>n.type===t).length}})`;
    btn.onclick = () => {{
        if (activeTypes.has(t)) {{ activeTypes.delete(t); btn.classList.remove('active'); }}
        else {{ activeTypes.add(t); btn.classList.add('active'); }}
        updateGraph();
    }};
    filterDiv.appendChild(btn);
}});

// Legend
const legendDiv = document.getElementById('legend');
Object.entries(typeColors).forEach(([t, c]) => {{
    if (types.includes(t)) {{
        legendDiv.innerHTML += `<div class="legend-item"><span class="legend-dot" style="background:${{c}}"></span>${{t}}</div>`;
    }}
}});

// Create simulation
const simulation = d3.forceSimulation(nodes)
    .force('link', d3.forceLink(links).id(d => d.id).distance(80).strength(0.3))
    .force('charge', d3.forceManyBody().strength(-200))
    .force('center', d3.forceCenter(width/2, height/2))
    .force('collision', d3.forceCollide().radius(d => Math.max(8, Math.sqrt(d.connections || 1) * 5) + 3)));

// Link rendering
const link = g.append('g').selectAll('line')
    .data(links).join('line')
    .attr('stroke', '#30363d').attr('stroke-width', 1.5)
    .attr('marker-end', 'url(#arrowhead)');

// Node rendering
const node = g.append('g').selectAll('g')
    .data(nodes).join('g')
    .call(d3.drag()
        .on('start', (event, d) => {{ if (!event.active) simulation.alphaTarget(0.3).restart(); d.fx = d.x; d.fy = d.y; }})
        .on('drag', (event, d) => {{ d.fx = event.x; d.fy = event.y; }})
        .on('end', (event, d) => {{ if (!event.active) simulation.alphaTarget(0); d.fx = null; d.fy = null; }})
    );

node.append('circle')
    .attr('r', d => Math.max(6, Math.sqrt(d.connections || 1) * 4))
    .attr('fill', d => typeColors[d.type] || '#8b949e')
    .attr('stroke', '#0d1117').attr('stroke-width', 1.5)
    .attr('opacity', 0.85);

// Labels for important nodes only
const nodeLabels = node.append('text')
    .text(d => d.connections > 3 ? d.id.split('(')[0].trim().substring(0, 30) : '')
    .attr('font-size', '10px').attr('fill', '#c9d1d9')
    .attr('dx', d => Math.max(8, Math.sqrt(d.connections || 1) * 4) + 4)
    .attr('dy', 3);

// Tooltip
const tooltip = document.getElementById('tooltip');
node.on('mouseover', (event, d) => {{
    tooltip.style.display = 'block';
    tooltip.style.left = (event.pageX + 12) + 'px';
    tooltip.style.top = (event.pageY - 12) + 'px';
    document.getElementById('tt-name').textContent = d.id;
    document.getElementById('tt-type').textContent = d.type + ' · ' + (d.connections || 0) + ' conexões';
}}).on('mouseout', () => {{
    tooltip.style.display = 'none';
}});

// Click to select node
node.on('click', (event, d) => {{
    event.stopPropagation();
    selectedNode = d;
    showNodeInfo(d);
    highlightConnected(d);
}});

svg.on('click', () => {{
    selectedNode = null;
    clearHighlight();
    document.getElementById('node-info').innerHTML = '<h3>Clique em um nó</h3><div class="meta">Selecione uma entidade</div>';
}});

function showNodeInfo(d) {{
    const infoDiv = document.getElementById('node-info');
    const connected = links.filter(l => l.source.id === d.id || l.target.id === d.id);
    let html = `<h3 style="color:${{typeColors[d.type] || '#c9d1d9'}}">${{d.id}}</h3>`;
    html += `<div class="meta">${{d.type}} · ${{d.connections || 0}} conexões</div>`;
    if (d.aliases && d.aliases.length > 0) {{
        html += `<div class="meta" style="margin-top:4px">Aliases: ${{d.aliases.join(', ')}}</div>`;
    }}
    html += `<div class="connections" style="margin-top:8px">`;
    connected.slice(0, 20).forEach(l => {{
        const other = l.source.id === d.id ? l.target : l.source;
        const direction = l.source.id === d.id ? '→' : '←';
        html += `<div class="conn-item">${{direction}} <span class="conn-type">${{l.predicate}}</span> ${{other.id}}</div>`;
    }});
    if (connected.length > 20) html += `<div class="meta">... e mais ${{connected.length - 20}} conexões</div>`;
    html += `</div>`;
    infoDiv.innerHTML = html;
}}

function highlightConnected(d) {{
    const connectedIds = new Set([d.id]);
    links.forEach(l => {{
        if (l.source.id === d.id || l.target.id === d.id) {{
            connectedIds.add(l.source.id);
            connectedIds.add(l.target.id);
        }}
    }});
    
    node.select('circle')
        .attr('opacity', n => connectedIds.has(n.id) ? 1 : 0.1)
        .attr('stroke', n => n.id === d.id ? '#fff' : '#0d1117')
        .attr('stroke-width', n => n.id === d.id ? 3 : 1.5);
    link.attr('opacity', l => (l.source.id === d.id || l.target.id === d.id) ? 1 : 0.05)
        .attr('stroke', l => (l.source.id === d.id || l.target.id === d.id) ? '#58a6ff' : '#30363d');
}}

function clearHighlight() {{
    node.select('circle')
        .attr('opacity', 0.85).attr('stroke', '#0d1117').attr('stroke-width', 1.5);
    link.attr('opacity', 1).attr('stroke', '#30363d');
}}

// Search
document.getElementById('search').addEventListener('input', (e) => {{
    searchTerm = e.target.value.toLowerCase();
    updateGraph();
}});

function updateGraph() {{
    const visible = nodes.filter(n => 
        activeTypes.has(n.type) && 
        (!searchTerm || n.id.toLowerCase().includes(searchTerm))
    );
    const visibleIds = new Set(visible.map(n => n.id));
    
    node.select('circle')
        .attr('opacity', n => (visibleIds.has(n.id) ? 0.85 : 0.05))
        .attr('r', n => Math.max(6, Math.sqrt(n.connections || 1) * 4));
    nodeLabels.text(d => (visibleIds.has(d.id) && d.connections > 3) ? d.id.split('(')[0].trim().substring(0, 30) : '');
    link.attr('opacity', l => (visibleIds.has(l.source.id) && visibleIds.has(l.target.id)) ? 1 : 0.02);
}}

// Tick
simulation.on('tick', () => {{
    link.attr('x1', d => d.source.x).attr('y1', d => d.source.y)
        .attr('x2', d => d.target.x).attr('y2', d => d.target.y);
    node.attr('transform', d => `translate(${{d.x}},${{d.y}})`);
}});

// Auto-fit
setTimeout(() => {{
    svg.transition().duration(750).call(
        zoom.transform,
        d3.zoomIdentity.translate(width/6, height/6).scale(0.6)
    );
}}, 2000);
</script>
</body>
</html>"""
    return html


def main():
    print("Loading graph data...")
    entities, triples = load_data()
    nodes, links = build_graph_data(entities, triples)
    
    print(f"Nodes: {len(nodes)}, Links: {len(links)}")
    
    html = generate_html(nodes, links, entities)
    output_path = OUTPUT_DIR / "knowledge_graph.html"
    output_path.write_text(html, encoding="utf-8")
    
    print(f"\n✅ Interactive graph saved to: {output_path}")
    print(f"   Open in browser: file://{output_path}")
    
    # Also save CSV for external use
    import csv
    with open(OUTPUT_DIR / "triples.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["subject", "predicate", "object"])
        for t in triples:
            writer.writerow([t["subject"], t["predicate"], t["object"]])
    
    with open(OUTPUT_DIR / "entities.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "type", "connections", "aliases"])
        connections = Counter()
        for t in triples:
            connections[t["subject"]] += 1
            connections[t["object"]] += 1
        for name, info in entities.items():
            aliases = "; ".join(info.get("aliases", []))
            writer.writerow([name, info.get("type", ""), connections.get(name, 0), aliases])
    
    print(f"✅ CSV exports saved to: {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()