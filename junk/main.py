import os

# The structure you defined
structure = {
    "directories": [
        "data/novels",
        "data/backstories",
        "data/splits",
        "src",
        "scripts",
        "outputs",
        "report"
    ],
    "files": [
        "README.md",
        "requirements.txt",
        ".env.example",
        "data/splits/train_ids.txt",
        "data/splits/test_ids.txt",
        "src/ingest.py",
        "src/chunking.py",
        "src/vector_store.py",
        "src/retrieval.py",
        "src/prompt.py",
        "src/llm.py",
        "src/classifier.py",
        "src/pipeline.py",
        "scripts/run_train.py",
        "scripts/run_inference.py",
        "scripts/evaluate.py",
        "outputs/results.csv"  # Placeholder
    ]
}

def create_structure():
    # 1. Create Directories
    for folder in structure["directories"]:
        os.makedirs(folder, exist_ok=True)
        print(f"✅ Created folder: {folder}")

    # 2. Create Empty Files
    for file in structure["files"]:
        if not os.path.exists(file):
            with open(file, 'w') as f:
                # Add a tiny comment so files aren't totally empty
                f.write(f"# {os.path.basename(file)}\n")
            print(f"📄 Created file:   {file}")
        else:
            print(f"⚠️  File exists:    {file}")

if __name__ == "__main__":
    create_structure()
    print("\n🚀 Project structure ready!")