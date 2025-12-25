import pathway as pw

def load_policies():
    policies = pw.io.fs.read("./policies", format = "text")
    return policies

if __name__ == "__main__":
    policies = load_policies()

    # Debug: print table schema
    print(policies.schema)

    # Debug: print contents (Pathway way)
    pw.debug.compute_and_print(policies)