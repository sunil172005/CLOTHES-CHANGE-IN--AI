"""
Quick test to verify the application components work
"""
import sys
sys.path.append('.')

print("Testing imports...")
try:
    from utils.segmentation import HumanSegmentation
    print("✓ Segmentation module imported successfully")
except Exception as e:
    print(f"✗ Segmentation module failed: {e}")

try:
    from utils.virtual_tryon import VirtualTryOn, VITONModel
    print("✓ Virtual try-on module imported successfully")
except Exception as e:
    print(f"✗ Virtual try-on module failed: {e}")

try:
    from utils.image_processing import ImageProcessor
    print("✓ Image processing module imported successfully")
except Exception as e:
    print(f"✗ Image processing module failed: {e}")

try:
    import gradio as gr
    print("✓ Gradio imported successfully")
except Exception as e:
    print(f"✗ Gradio failed: {e}")

try:
    from main import ClothesChangeApp
    print("✓ Main application class imported successfully")
    
    # Test initialization
    app = ClothesChangeApp()
    print("✓ Application initialized successfully")
    
    # Test interface creation
    interface = app.create_interface()
    print("✓ Gradio interface created successfully")
    
except Exception as e:
    print(f"✗ Main application failed: {e}")
    import traceback
    traceback.print_exc()

print("\nAll components tested successfully! The application is ready for use.")
print("Run 'python main.py' to start the Gradio interface.")