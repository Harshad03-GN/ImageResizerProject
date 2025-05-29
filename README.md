# 🖼️ Image Resizer with Azure Blob Storage & GitHub Actions CI/CD

This is a Python-based image resizer that processes images from Azure Blob Storage and saves resized versions back to Azure. It also includes a GitHub Actions workflow for DevOps-style automation.

---

## 📌 Features

- Resize `.jpg`, `.png` images to a fixed or custom size
- Uses **Azure Blob Storage** to read/write images from the cloud
- CI/CD integration with **GitHub Actions**
- Easy to extend with GUI, API, or containerization (Docker)

---

## ☁️ Technologies Used

- Python 3.11
- Pillow (image processing)
- Azure Blob Storage SDK
- GitHub Actions (CI/CD)
- Git (for version control)

---

## 🚀 How It Works

1. Upload images to Azure Blob container named `input`
2. Run the script (`main.py`) or trigger it via CI/CD
3. Resized images will be saved to a Blob container named `output`

---

## 🧪 Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/image-resizer-azure-devops.git
cd image-resizer-azure-devops
