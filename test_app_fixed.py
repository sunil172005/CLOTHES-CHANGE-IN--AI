"""
Test Script for Clothes Change Application
This script tests the functionality of the clothes change application
with sample images.
"""
import os
import sys
from PIL import Image
import numpy as np

# Add project root to path
sys.path.append(os.path.join(os.path.dirname(__file__)))

from utils.segmentation import HumanSegmentation
from utils.virtual_tryon import VirtualTryOn, VITONModel
from utils.image_processing import ImageProcessor

def create_sample_images():
    """
    Create sample images for testing if none exist
    """
    os.makedirs('assets', exist_ok=True)
    
    # Create a simple sample person image (simulated)
    person_img = Image.new('RGB', (400, 600), color='lightblue')
    # Draw a simple person shape (this is just for testing the pipeline)
    person_np = np.array(person_img)
    
    # Draw a head
    cv2 = __import__('cv2')
    cv2.circle(person_np, (200, 150), 50, (255, 255, 255), -1)  # Head
    
    # Draw body with some clothing
    cv2.rectangle(person_np, (150, 200), (250, 400), (0, 0, 255), -1)  # Red clothing
    
    # Draw limbs
    cv2.rectangle(person_np, (100, 250), (150, 350), (255, 255, 255), -1)  # Left arm
    cv2.rectangle(person_np, (250, 250), (300, 350), (255, 255, 255), -1)  # Right arm
    cv2.rectangle(person_np, (175, 400), (200, 550), (255, 255, 255), -1)  # Left leg
    cv2.rectangle(person_np, (200, 400), (225, 550), (255, 255, 255), -1)  # Right leg
    
    person_img = Image.fromarray(person_np)
    person_img.save('assets/sample_person.jpg')
    
    # Create a sample clothes image
    clothes_img = Image.new('RGB', (300, 300), color='green')
    clothes_img.save('assets/sample_clothes.jpg')
    
    print("Sample images created in assets/ folder")

def test_segmentation():
    """
    Test the segmentation module
    """
    print("\n=== Testing Segmentation Module ===")
    
    try:
        seg_model = HumanSegmentation(device='cpu')  # Use CPU for testing
        
        # Create or load sample image
        if not os.path.exists('assets/sample_person.jpg'):
            create_sample_images()
        
        # Test segmentation
        mask, segmented = seg_model.segment_human('assets/sample_person.jpg')
        
        print(f"Segmentation successful!")
        print(f"Mask shape: {mask.shape}")
        print(f"Mask unique values: {np.unique(mask)}")
        
        # Test clothing segmentation
        body_mask, clothing_mask = seg_model.segment_clothing_regions('assets/sample_person.jpg')
        print(f"Clothing segmentation successful!")
        print(f"Body mask shape: {body_mask.shape}")
        print(f"Clothing mask shape: {clothing_mask.shape}")
        
        return True
        
    except Exception as e:
        print(f"Segmentation test failed: {str(e)}")
        return False

def test_virtual_tryon():
    """
    Test the virtual try-on module
    """
    print("\n=== Testing Virtual Try-On Module ===")
    
    try:
        # Initialize try-on model
        tryon_model = VirtualTryOn(device='cpu')
        
        # Create sample images if needed
        if not os.path.exists('assets/sample_person.jpg'):
            create_sample_images()
        if not os.path.exists('assets/sample_clothes.jpg'):
            create_sample_images()
        
        # Load images
        person_img = Image.open('assets/sample_person.jpg')
        clothes_img = Image.open('assets/sample_clothes.jpg')
        
        # Create a dummy mask for testing
        dummy_mask = np.zeros((person_img.height, person_img.width), dtype=np.uint8)
        dummy_mask[200:400, 150:250] = 1  # Clothing area
        
        # Test basic clothes replacement
        result = tryon_model._basic_clothes_replacement(
            person_img, clothes_img, dummy_mask
        )
        
        print("Virtual try-on test successful!")
        print(f"Result image size: {result.size}")
        
        # Save result for inspection
        result.save('assets/test_result_basic_tryon.jpg')
        
        return True
        
    except Exception as e:
        print(f"Virtual try-on test failed: {str(e)}")
        return False

def test_image_processing():
    """
    Test the image processing module
    """
    print("\n=== Testing Image Processing Module ===")
    
    try:
        processor = ImageProcessor()
        
        # Create sample images
        if not os.path.exists('assets/sample_person.jpg'):
            create_sample_images()
        
        person_img = Image.open('assets/sample_person.jpg')
        modified_img = Image.new('RGB', person_img.size, color='yellow')
        
        # Create dummy masks
        body_mask = np.zeros((person_img.height, person_img.width), dtype=bool)
        body_mask[100:200, 150:250] = True  # Simulated face area
        clothing_mask = np.zeros((person_img.height, person_img.width), dtype=np.uint8)
        clothing_mask[200:400, 150:250] = 1  # Simulated clothing area
        
        # Test face preservation
        result_face = processor.preserve_face_features(
            person_img, modified_img, body_mask
        )
        print("Face preservation test successful!")
        
        # Test skin tone maintenance
        result_skin = processor.maintain_skin_tone(
            person_img, modified_img, body_mask
        )
        print("Skin tone maintenance test successful!")
        
        # Test realism enhancement
        result_realism = processor.enhance_realism(
            modified_img, clothing_mask, body_mask
        )
        print("Realism enhancement test successful!")
        
        # Save results
        result_face.save('assets/test_result_face_preserve.jpg')
        result_skin.save('assets/test_result_skin_tone.jpg')
        result_realism.save('assets/test_result_realism.jpg')
        
        return True
        
    except Exception as e:
        print(f"Image processing test failed: {str(e)}")
        return False

def test_full_pipeline():
    """
    Test the full pipeline integration
    """
    print("\n=== Testing Full Pipeline Integration ===")
    
    try:
        # Initialize all components
        segmentation = HumanSegmentation(device='cpu')
        tryon = VirtualTryOn(device='cpu')
        processor = ImageProcessor()
        
        # Create sample images
        if not os.path.exists('assets/sample_person.jpg'):
            create_sample_images()
        if not os.path.exists('assets/sample_clothes.jpg'):
            create_sample_images()
        
        # Load images
        person_img = Image.open('assets/sample_person.jpg').convert('RGB')
        clothes_img = Image.open('assets/sample_clothes.jpg').convert('RGB')
        
        # Step 1: Segment the person
        human_mask, segmented_person = segmentation.segment_human(person_img)
        print("✓ Step 1: Human segmentation completed")
        
        # Step 2: Identify body and clothing regions
        body_mask, clothing_mask = segmentation.segment_clothing_regions(person_img)
        print("✓ Step 2: Body/clothing region identification completed")
        
        # Step 3: Apply virtual try-on (using basic method for testing)
        viton_model = VITONModel()
        warped_clothes = viton_model.warp_clothes(person_img, clothes_img)
        result_image = viton_model.fuse_features(
            person_img, warped_clothes, body_mask, clothing_mask
        )
        print("✓ Step 3: Virtual try-on completed")
        
        # Step 4: Process image for realism
        # Preserve face features
        result_image = processor.preserve_face_features(
            person_img, result_image
        )
        
        # Maintain skin tone consistency
        result_image = processor.maintain_skin_tone(
            person_img, result_image, body_mask
        )
        
        # Enhance realism with lighting and shadows
        result_image = processor.enhance_realism(
            result_image, clothing_mask, body_mask
        )
        print("✓ Step 4: Image processing completed")
        
        # Save final result
        result_image.save('assets/test_result_full_pipeline.jpg')
        print("✓ Full pipeline test successful!")
        print(f"Final image saved as 'assets/test_result_full_pipeline.jpg'")
        
        return True
        
    except Exception as e:
        print(f"Full pipeline test failed: {str(e)}")
        return False

def main():
    """
    Main test function
    """
    print("Starting Clothes Change Application Tests...\n")
    
    # Create sample images first
    create_sample_images()
    
    # Run all tests
    tests = [
        ("Segmentation Module", test_segmentation),
        ("Virtual Try-On Module", test_virtual_tryon),
        ("Image Processing Module", test_image_processing),
        ("Full Pipeline Integration", test_full_pipeline)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n{'='*50}")
        print(f"Running {test_name}...")
        print('='*50)
        
        success = test_func()
        results.append((test_name, success))
    
    # Print summary
    print(f"\n{'='*50}")
    print("TEST SUMMARY")
    print('='*50)
    
    all_passed = True
    for test_name, success in results:
        status = "PASS" if success else "FAIL"
        print(f"{test_name}: {status}")
        if not success:
            all_passed = False
    
    print(f"\nOverall Result: {'ALL TESTS PASSED' if all_passed else 'SOME TESTS FAILED'}")
    
    if all_passed:
        print("\n🎉 The clothes change application is ready for use!")
        print("Run 'python main.py' to start the Gradio interface.")
    else:
        print("\n⚠️  Some tests failed. Please check the implementation.")

if __name__ == "__main__":
    main()