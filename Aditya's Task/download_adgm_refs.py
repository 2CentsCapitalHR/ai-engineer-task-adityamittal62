import requests
import os

ADGM_URLS = [
    # Company Formation - Resolution for Incorporation (LTD - Multiple Shareholders)
    "https://assets.adgm.com/download/assets/adgm-ra-resolution-multipleincorporate-shareholders-LTDincorporationv2.docx/186a12846c3911efa4e6c6223862cd87",

    # Employment & HR - Standard Employment Contract Template (2024 update)
    "https://assets.adgm.com/download/assets/ADGM+Standard+Employment+Contract+Template+-+ER+2024+(Feb+2025).docx/ee14b252edbe11efa63b12b3a30e5e3a",

    # Employment & HR - Standard Employment Contract Template (2019 short version)
    "https://assets.adgm.com/download/assets/ADGM+Standard+Employment+Contract+-+ER+2019+-+Short+Version+(May+2024).docx/33b57a92ecfe11ef97a536cc36767ef8",

    # Data Protection - Appropriate Policy Document Template
    "https://www.adgm.com/documents/office-of-data-protection/templates/adgm-dpr-2021-appropriate-policy-document.pdf",

    # ADGM Company Set-up Checklist – Company Setup (Various Entities)
    "https://www.adgm.com/documents/registration-authority/registration-and-incorporation/checklist/branch-non-financial-services-20231228.pdf",

    # ADGM Company Set-up Checklist – Private Company Limited
    "https://www.adgm.com/documents/registration-authority/registration-and-incorporation/checklist/private-company-limited-by-guarantee-non-financial-services-20231228.pdf",

    # Regulatory Template - Shareholder Resolution – Amendment of Articles
    "https://assets.adgm.com/download/assets/Templates_SHReso_AmendmentArticles-v1-20220107.docx/97120d7c5af911efae4b1e183375c0b2?forcedownload=1"
]

os.makedirs("adgm_corpus", exist_ok=True)

for url in ADGM_URLS:
    filename = os.path.join("adgm_corpus", url.split("/")[-1].split("?")[0])
    print(f"Downloading {url} -> {filename}")
    try:
        r = requests.get(url)
        if r.status_code == 200:
            with open(filename, "wb") as f:
                f.write(r.content)
        else:
            print(f"Failed to download: {url} (Status {r.status_code})")
    except Exception as e:
        print(f"Error downloading {url}: {e}")
