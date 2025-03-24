import kagglehub

# Download latest version
path = kagglehub.dataset_download("miadul/brain-tumor-dataset")

print("Path to dataset files:", path)
