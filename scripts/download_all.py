#!/usr/bin/env python3
"""Download all PDFs from CADE Google Drive folder, one by one with delays."""
import os
import time
import subprocess
import json

FOLDER_ID = "1xEVFOvvtetmuxODPDZmf92OPaTjBm4-T"
DEST_DIR = os.path.expanduser("~/brain_cade/raw/notas")

os.makedirs(DEST_DIR, exist_ok=True)

# List all files in the folder using gdown's internal API
result = subprocess.run(
    ["python3", "-c", f"""
import json
from googleapiclient.discovery import build
from googleapiclient.http import build_http

# Use gdown's fetcher to list files
import gdown
import re

url = "https://drive.google.com/drive/folders/{FOLDER_ID}"
contents = gdown.download._download_and_parse_google_drive_file_list(url, gdown.download._get_session())
files = []
for f in contents:
    files.append({{"id": f[0], "name": f[1]}})
print(json.dumps(files))
"""],
    capture_output=True, text=True, timeout=30
)

# Alternative: just use the file IDs we already saw in the gdown output
# These were extracted from the previous gdown runs
FILE_IDS = {
    "1P3LwrG8vBJKzOp47GUwrofycK6KG2Lna": "Nota_T_cnica_n__01_2013___Ato_de_Concentra__o_n__08012_010038_2010_43.pdf",
    "1IpG8dvZm2nGVtrD1mdAfEnbxc-Id8PTm": "Nota_T_cnica_n__01_2015___Ato_de_Concentra__o_n__08700_009732_2014_93.pdf",
    "1t2yh8qY3UqviKG4iUTX8FwQn6IL2FvRN": "Nota_T_cnica_n__02_2011___Ato_de_Concentra__o_n__08012_004654_2009_21.pdf",
    "12pUoDMZ1uTbeqSeyQnxjChMUNOVX3yMh": "Nota_T_cnica_n__02_2014___Ato_de_Concentra__o_n__08700_004065_2012_91.pdf",
    "1saxZQqwgfzqTekaWi4m2iHtWP-BgNZWM": "Nota_T_cnica_n__02_2015___Ato_de_Concentra__o_n__08700_009711_2014_78.pdf",
    "180NcMetswUGCgdCUWk8PLbUN4gFyjSgF": "Nota_T_cnica_n__05_2017___Ato_de_Concentra__o_n__08700_006444_2016_49.pdf",
    "1gNf7--UQvaaiMYCRBy2fORwfXk54i5Ey": "Nota_T_cnica_n__06_2014___Ato_de_Concentra__o_n__08700_005447_2013_12.pdf",
    "19u2CSpVFYm_7Ff8epeXP-4YjWmmecBpz": "Nota_T_cnica_n__07_2016___Ato_de_Concentra__o_n__08700_010266_2015_70.pdf",
    "18Tr9eoX2721dNSVFCcjR_HyyyJPqSWjM": "Nota_T_cnica_n__07_2017___Ato_de_Concentra__o_n__08700_006185_2016_56.pdf",
    "1_aqbc4Bkl7aH8JuKShrEDMHc_nW6Pi9b": "Nota_T_cnica_n__07___Ato_de_Concentra__o_n__08700_002346_2019_85.pdf",
    "15gJrho_I6pLtC8C0lyUtQwPKXIWNwSX1": "Nota_T_cnica_n__10_2016___Ato_de_Concentra__o_n__08700_010790_2015_41.pdf",
    "1FOsyGftvXO0x3cipXg5Z5U7cqPhpLpVW": "Nota_T_cnica_n__10___Ato_de_Concentra__o_n__08700_002346_2019_85.pdf",
    "1dGE4nurwQQ9tWL4Q61D6GgIDiTG7x8Ea": "Nota_T_cnica_n__12_2014___Ato_de_Concentra__o_n__08700_000811_2014_39.pdf",
    "1-3pE1e9ckRuyV7NCT0RE-Yn9av86u7n6": "Nota_T_cnica_n__12_2015___Ato_de_Concentra__o__n__08700_010224_2014_58.pdf",
    "1LqTv3x8aXF0rIYRxFPxjg2GzcfFPoOZJ": "Nota_T_cnica_n__13___Ato_de_Concentra__o_n__8700_009924_2013_19.pdf",
    "1i86KQ1GH46XdPGjpPToV0XmhvptSyVCo": "Nota_T_cnica_n__14___Ato_de_Concentra__o_n__08700_005700_2021_48.pdf",
    "1uS2tbJ2fVGp3QRyl32i-a1tjworxeA0h": "Nota_T_cnica_n__15_2016___Ato_de_Concentra__o_n__08700_010790_2015_41.pdf",
    "1HNpLMn04_RnkOxy2hw_drMRXQMzRwwpy": "Nota_T_cnica_n__15___Ato_de_Concentra__o_n__08700_001128_2023_18.pdf",
    "1PgsV-pf2nRvBsSuA3iab1k7CuEd7duG3": "Nota_T_cnica_n__15___Ato_de_Concentra__o_n__08700_001128_2023_18_doc2.pdf",
    "1IX2U8SBYDzTmlY4jx8LvijQVfhwUheIL": "Nota_T_cnica_n__16_2016___Ato_de_Concentra__o_n__08700_003861_2016_30.pdf",
    "1LnOFChgkuPpGhWa-IZL4V5R74U-vzyR1": "Nota_T_cnica_n__16___Ato_de_Concentra__o_n__08700_009924_2013_19.pdf",
    "1HCcFNWhLW-jzPlD1mCrMfAe6qSOj7mrj": "Nota_T_cnica_n__17_2014___Ato_de_Concentra__o_n__08700_009924_2013_19.pdf",
    "18Wg-bo9fA4X0OS6RaFPpppbNWKyUKqu_": "Nota_T_cnica_n__18_2015___Ato_de_Concentra__o_n__08700_009465_2014_54.pdf",
    "1tsZsU76p4H2dsdlc6nbIaXsoDjXz-NqZ": "Nota_T_cnica_n__18___Ato_de_Concentra__o_n__08700_000166_2018_88.pdf",
    "1qk-Qp0rhzK6xIC5C1aBMVK7Tas9LvZR9": "Nota_T_cnica_n__19_2015___Ato_de_Concentra__o_n__08700_009988_2014_09.pdf",
    "1i0IWZ4xsPErVE2D3yjnGFtXo9BUQbb5x": "Nota_T_cnica_n__19_2017___Ato_de_Concentra__o_n__08700_007553_2016_83.pdf",
    "1_ZcGR_fUgTOIXL-PhlTE6Cm3w42U1lp8": "Nota_T_cnica_n__20___Ato_de_Concentra__o_n__08700_003662_2018_93.pdf",
    "1WiUiUW7pB1aYOzUrBT-VvX9PsavBjUod": "Nota_T_cnica_n__20___Ato_de_Concentra__o_n__08700_006345_2018_29.pdf",
    "1MWuzJvSfzYGUnJWbgro24LHcX49sK8KV": "Nota_T_cnica_n__21_2014___Ato_de_Concentra__o_n__08700_000344_2014_47.pdf",
    "15iaXlmcH6wRVIZhUBlIrhd0QkIaaVnwg": "Nota_T_cnica_n__22___Ato_de_Concentra__o_n__08700_006512_2021_37.pdf",
    "1HpFwZUAJ3wo_ylsXlb7sn7sIotXganaP": "Nota_T_cnica_n__23_2014___Ato_de_Concentra__o_n__08700_004185_2014_50.pdf",
    "1wpUcDuhcKLW7soOKMQ-G3bHymuyFaOWt": "Nota_T_cnica_n__24_2014___Ato_de_Concentra__o_n__08700_000436_2014_27.pdf",
    "1j5rt-ZqfPx2wDf9kpweM72hokspmNEvW": "Nota_T_cnica_n__24___Ato_de_Concentra__o_n__08700_002855_2022_11.pdf",
    "19-czNP2McjtqgoECnMFNtL225N0FZ_Dk": "Nota_T_cnica_n__25_2017___Ato_de_Concentra__o_n__08700_006444_2016_49.pdf",
    "1Q5ndjh6YDpGAQIBtNO2PN187FANc5e7R": "Nota_T_cnica_n__26___Ato_de_Concentra__o_n__08700_000149_2021_46.pdf",
    "10cJs-M51apPN_RZ8hO1ZBvN1zNxCtACP": "Nota_T_cnica_n__28_2017___Ato_de_Concentra__o_n__08700_001390_2017_14.pdf",
    "16mtzQUJpWqF9T_TnTmwU4t12DAcdfVtc": "Nota_T_cnica_n__29_2017___Ato_de_Concentra__o_n__08700_002155_2017_51.pdf",
    "1gvAEuWZ9DK9dCApjkDR2y3JUriWF7_8o": "Nota_T_cnica_n__29___Ato_de_Concentra__o_n__08700_000472_2020_39.pdf",
    "1p_Cf8iG-TEbAEcprhmuCMuXfwuyXVcif": "Nota_T_cnica_n__29___Ato_de_Concentra__o_n__08700_003244_2019_87.pdf",
    "12PxB4sk0K3kUgF8e9H-0nhLspHcBzTQz": "Nota_T_cnica_n__2___Ato_de_Concentra__o_n__08700_000869_2015_63.pdf",
    "1_98yT9jroYiqXJ3BE6cXLO6AEwLdKwZl": "Nota_T_cnica_n__2___Ato_de_Concentra__o_n__08700_002165_2017_97.pdf",
    "1g4v4mOyt8wUZ5sL0y81SFM_1V6IZGROh": "Nota_T_cnica_n__30_2016___Ato_de_Concentra__o_n__08700_003462_2016_79.pdf",
    "1uEJWDdjPGqzfD2eykQTl-io7wiAIbqw-": "Nota_T_cnica_n__30_2017___Ato_de_Concentra__o_n__08700_002165_2017_97.pdf",
    "1CoEoltz8ytTmmKnTEPeyi9JpIVjZ739F": "Nota_T_cnica_n__30___Ato_de_Concentra__o_n__08700_001134_2020_14.pdf",
    "1Uj5oj3_3Stjb5NEO8oA9S66-R23YfQqZ": "Nota_T_cnica_n__30___Ato_de_Concentra__o_n__08700_003959_2022_35.pdf",
    "17mJm8_3tIlmYfKXQIAOQZXq7Bb2stiRE": "Nota_T_cnica_n__30___Ato_de_Concentra__o_n__08700_004426_2020_17.pdf",
    "1Qx7ewUeIsertXZtbrDWbG-1N638iDD0q": "Nota_T_cnica_n__32_2017___Ato_de_Concentra__o_n__08012_002018_2010_07.pdf",
    "1SaYs2Hv18fjRLOYIktjdAxzEmwhKFYBq": "Nota_T_cnica_n__32___Ato_de_Concentra__o_n__08700_004046_2022_36.pdf",
    "13Q4VGPFGi39nfx_B-Yqxm1OoxAkUD5ct": "Nota_T_cnica_n__33_2017___Ato_de_Concentra__o_n__08700_001097_2017_49.pdf",
    "1c1fXNIlgYlQo5x65xQGyCimoH1aE0AJk": "Nota_T_cnica_n__34___Ato_de_Concentra__o_n__08700_000726_2021_08.pdf",
    "1NOnzQOtWU7A-F3UErknFc_e1r2PTk_Up": "Nota_T_cnica_n__35_2016___Ato_de_Concentra__o_n__08700_004211_2016_10.pdf",
    "1CJD3xj9PzJn30q2oKYCPMAWbB-lykurX": "Nota_T_cnica_n__37___Ato_de_Concentra__o_n__08700_001846_2020_33.pdf",
    "1A7ezfUjBEHt8byM0fukRi7tVAc2SJFU0": "Nota_T_cnica_n__38_2016___Ato_de_Concentra__o_n__08700_004860_2016_11.pdf",
    "1qKqz_hFmNLkh9-ArVwPLsk150p_0XPW6": "Nota_T_cnica_n__39___Ato_de_Concentra__o_n__08700_005979_2017_83.pdf",
    "10tM1Tt-2fqlceVFlt2IzX0pibSkG1OyT": "Nota_T_cnica_n__3___Ato_de_Concentra__o_n__08700_005137_2017_21.pdf",
    "1Ec5TmZgfzQ-ov-88tCzVLz7_PuwxVDOA": "Nota_T_cnica_n__40___Ato_de_Concentra__o_n__08700_003662_2018_93.pdf",
    "1mpN5wWbwhYLNxZiTI44QCiQDW8HjyqZF": "Nota_T_cnica_n__41_2016___Ato_de_Concentra__o_n__08700_005683_2016_81.pdf",
    "1BWhKkKPpmrbvoX7k2NCkq0F5m2f2HZvN": "Nota_T_cnica_n__44___Ato_de_Concentra__o_n__08700_003594_2021_68.pdf",
    "1zNsKS7FnlMO_9n3dx9OjQgYE6Ica5Nc-": "Nota_T_cnica_n__47___Ato_de_Concentra__o_n__08700_002569_2020_86.pdf",
    "16_xnsoabi3c-5TkYfElJhEEBaVTijQcm": "Nota_T_cnica_n__5___Ato_de_Concentra__o_n__08700_004162_2018_79.pdf",
    "19MZyF4R08bS0wBFA6HQGUFgWa53TV05Y": "Nota_T_cnica_n__7___Ato_de_Concentra__o_n__08700_005137_2017_21.pdf",
}

downloaded = 0
skipped = 0
failed = []

for file_id, filename in FILE_IDS.items():
    dest = os.path.join(DEST_DIR, filename)
    if os.path.exists(dest):
        skipped += 1
        continue
    
    url = f"https://drive.google.com/uc?id={file_id}"
    print(f"Downloading {filename}...", flush=True)
    
    for attempt in range(3):
        try:
            result = subprocess.run(
                ["gdown", url, "-O", dest, "--quiet"],
                capture_output=True, text=True, timeout=120
            )
            if result.returncode == 0 and os.path.exists(dest) and os.path.getsize(dest) > 1000:
                downloaded += 1
                break
            else:
                print(f"  Attempt {attempt+1} failed, retrying...", flush=True)
                time.sleep(5)
        except subprocess.TimeoutExpired:
            print(f"  Attempt {attempt+1} timed out, retrying...", flush=True)
            time.sleep(5)
    else:
        failed.append(filename)
        print(f"  FAILED: {filename}", flush=True)
    
    time.sleep(2)  # rate limit protection

# Count final
all_pdfs = [f for f in os.listdir(DEST_DIR) if f.endswith('.pdf')]
print(f"\n=== DONE ===")
print(f"Total PDFs: {len(all_pdfs)}")
print(f"Downloaded this run: {downloaded}")
print(f"Skipped (already existed): {skipped}")
print(f"Failed: {len(failed)}")
if failed:
    print(f"Failed files:")
    for f in failed:
        print(f"  - {f}")