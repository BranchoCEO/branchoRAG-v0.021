import branchorag

# Change "." to a specific path like "C:/Users/Name/Projects/Test" to scan elsewhere
SCAN_PATH = "." 
MEMORY_FILE = "brancho_memory.json"

def run_brain():
    print("--- BranchoRAG v0.01: Active ---")

    try:
        # 1. Initialize the RAG system
        rag = branchorag.BranchoRAG()

        # 2. Tell the AI to look at the project folder
        print(f"Scanning folder: {SCAN_PATH}...")
        rag.scan_folder(SCAN_PATH)
        
        # This will now show a much smaller, cleaner number!
        print(f"  Found {rag.node_count()} relevant file(s).")

        # 3. Save the findings to your SSD
        rag.save_memory(MEMORY_FILE)
        print(f"✅ Success: BranchoRAG has mapped your project to {MEMORY_FILE}.")

    except Exception as e:
        print(f"❌ BranchoRAG failed: {e}")
        raise

if __name__ == "__main__":
    run_brain()
