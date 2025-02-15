import xml.etree.ElementTree as ET
from collections import Counter
import os

labels = [
    "UL3M_healthy", "UL2M_healthy", "UL1M_healthy", "UL2BC_healthy", "UL1BC_healthy", "ULC_healthy", "ULLI_healthy", "ULCI_healthy", "UR3M_healthy", "UR2M_healthy", "UR1M_healthy", "UR2BC_healthy", "UR1BC_healthy", "URC_healthy", "URLI_healthy", "URCI_healthy", "LL3M_healthy", "LL2M_healthy", "LL1M_healthy", "LL2BC_healthy", "LL1BC_healthy", "LLC_healthy", "LLLI_healthy", "LLCI_healthy", "LR3M_healthy", "LR2M_healthy", "LR1M_healthy", "LR2BC_healthy", "LR1BC_healthy", "LRC_healthy", "LRLI_healthy", "LRCI_healthy", "UL3M_sdecay", "UL2M_sdecay", "UL1M_sdecay", "UL2BC_sdecay", "UL1BC_sdecay", "ULC_sdecay", "ULLI_sdecay", "ULCI_sdecay", "UR3M_sdecay", "UR2M_sdecay", "UR1M_sdecay", "UR2BC_sdecay", "UR1BC_sdecay", "URC_sdecay", "URLI_sdecay", "URCI_sdecay", "LL3M_sdecay", "LL2M_sdecay", "LL1M_sdecay", "LL2BC_sdecay", "LL1BC_sdecay", "LLC_sdecay", "LLLI_sdecay", "LLCI_sdecay", "LR3M_sdecay", "LR2M_sdecay", "LR1M_sdecay", "LR2BC_sdecay", "LR1BC_sdecay", "LRC_sdecay", "LRLI_sdecay", "LRCI_sdecay", "UL3M_mdecay", "UL2M_mdecay", "UL1M_mdecay", "UL2BC_mdecay", "UL1BC_mdecay", "ULC_mdecay", "ULLI_mdecay", "ULCI_mdecay", "UR3M_mdecay", "UR2M_mdecay", "UR1M_mdecay", "UR2BC_mdecay", "UR1BC_mdecay", "URC_mdecay", "URLI_mdecay", "URCI_mdecay", "LL3M_mdecay", "LL2M_mdecay", "LL1M_mdecay", "LL2BC_mdecay", "LL1BC_mdecay", "LLC_mdecay", "LLLI_mdecay", "LLCI_mdecay", "LR3M_mdecay", "LR2M_mdecay", "LR1M_mdecay", "LR2BC_mdecay", "LR1BC_mdecay", "LRC_mdecay", "LRLI_mdecay", "LRCI_mdecay"
]

def parse_annotation(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    label_counts = Counter({label: 0 for label in labels})
    
    for obj in root.findall(".//object"):
        label = obj.find("name").text
        if label in label_counts:
            label_counts[label] += 1
    
    return label_counts

def parse_annotations_in_folder(folder_path):
    total_counts = Counter({label: 0 for label in labels})
    
    for file in os.listdir(folder_path):
        if file.endswith(".xml"):
            file_path = os.path.join(folder_path, file)
            total_counts.update(parse_annotation(file_path))
    
    return total_counts

if __name__ == "__main__":
    folder_path = "C:\\bsu_thesis\\Tensorflow\\workspace\\images\\test"  # Change this to the path of your folder
    label_counts = parse_annotations_in_folder(folder_path)
    
    for label, count in label_counts.items():
        print(f"{label}: {count}")
