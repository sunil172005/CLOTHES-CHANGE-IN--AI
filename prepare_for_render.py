"""
Script to prepare the AI Clothes Changer project for Render deployment
"""
import os
import shutil
import sys

def prepare_deployment():
    print("Preparing AI Clothes Changer for Render deployment...")
    print("="*60)
    
    # Check if required files exist
    required_files = [
        'main.py',
        'requirements.txt',
        'requirements_render.txt',
        'Dockerfile',
        'utils/segmentation.py',
        'utils/virtual_tryon.py',
        'utils/image_processing.py'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print("❌ Missing required files:")
        for file in missing_files:
            print(f"   - {file}")
        return False
    else:
        print("✅ All required files present")
    
    # Create deployment package
    print("\n📦 Creating deployment-ready package...")
    
    # List all files that will be included
    deployment_files = [
        'main.py',
        'requirements_render.txt',
        'Dockerfile',
        'utils/segmentation.py',
        'utils/virtual_tryon.py',
        'utils/image_processing.py',
        'README.md',
        'RENDER_DEPLOYMENT_GUIDE.md'
    ]
    
    print("\n📋 Files to be included in deployment:")
    for file in deployment_files:
        if os.path.exists(file):
            print(f"   ✓ {file}")
        else:
            print(f"   ❌ {file}")
    
    print(f"\n📝 Deployment instructions:")
    print(f"   1. Create a GitHub repository with this code")
    print(f"   2. Connect your GitHub repo to Render")
    print(f"   3. Use the following settings:")
    print(f"      - Environment: Python")
    print(f"      - Build Command: pip install -r requirements_render.txt")
    print(f"      - Start Command: python main.py")
    print(f"      - Region: Your preferred region")
    print(f"      - Instance Type: Starter or Pro (recommended for AI apps)")
    print(f"   4. Add environment variables:")
    print(f"      - PORT: 10000")
    print(f"      - GRADIO_SERVER_NAME: 0.0.0.0")
    print(f"      - PYTHON_VERSION: 3.10")
    
    print(f"\n⚠️  Important Notes:")
    print(f"   - This AI application is resource-intensive")
    print(f"   - Free tier may not be sufficient for proper operation")
    print(f"   - Recommend Starter plan ($7/month) or higher")
    print(f"   - Initial model downloads may take several minutes")
    print(f"   - Consider using Hugging Face Spaces for initial testing")
    
    print(f"\n🌐 Alternative Deployment Platforms:")
    print(f"   1. Hugging Face Spaces (free, ML-optimized)")
    print(f"   2. Google Colab (for testing)")
    print(f"   3. AWS/GCP (more resources)")
    
    print("\n✅ Preparation complete!")
    print("Follow the RENDER_DEPLOYMENT_GUIDE.md for detailed instructions.")
    
    return True

if __name__ == "__main__":
    prepare_deployment()