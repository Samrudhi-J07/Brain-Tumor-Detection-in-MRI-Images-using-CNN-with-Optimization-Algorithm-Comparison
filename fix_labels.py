import os

label_path = "train/labels"   # ✅ FIXED PATH

for file in os.listdir(label_path):
    if file.endswith(".txt"):
        full_path = os.path.join(label_path, file)

        with open(full_path, "r") as f:
            lines = f.readlines()

        # remove NO_tumor (class 0)
        new_lines = [l for l in lines if not l.startswith("0 ")]

        if new_lines:
            with open(full_path, "w") as f:
                f.writelines(new_lines)

print("✅ Fixed labels!")