# AI-Powered Virtual Clothes Changer

A Python-based AI project that enables virtual clothes changing in human images using advanced computer vision techniques.

## Features

- **Input**: One person image (JPG/PNG format)
- **Output**: Same person with different clothes
- **Preservation**: Face, body pose, and skin tone remain unchanged
- **Technology**: Uses Stable Diffusion for realistic clothing replacement
- **Alternative Approach**: VITON-based virtual try-on model implementation
- **Segmentation**: Human segmentation to separate body and clothes
- **Realism**: Generates realistic shadows and lighting effects
- **UI**: Simple Gradio-based web interface

## Installation

1. Clone or download this repository to your local machine
2. Navigate to the project directory
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Dependencies

The project uses the following key libraries:

- `torch`, `torchvision` - PyTorch framework
- `diffusers` - Hugging Face diffusion models
- `transformers` - Hugging Face transformer models
- `Pillow` - Image processing
- `opencv-python` - Computer vision operations
- `gradio` - Web interface
- `segmentation-models-pytorch` - Semantic segmentation models
- `numpy`, `scikit-image` - Scientific computing

## Usage

### Running the Application

1. Make sure you have installed all dependencies
2. Run the main application:

```bash
python main.py
```

3. The application will start a local web server and provide a URL to access the interface
4. Access the interface through your web browser
5. Upload a person image and a clothes image
6. Click "Change Clothes" to see the result

### Sample Images

Place sample images in the `assets/` folder for easy access.

## Project Structure

```
├── main.py                 # Main application with Gradio UI
├── requirements.txt        # Required Python packages
├── models/                 # Trained model weights (will be downloaded automatically)
├── utils/
│   ├── segmentation.py     # Human segmentation module
│   ├── virtual_tryon.py    # Virtual try-on implementation
│   └── image_processing.py # Image enhancement and processing
└── assets/                 # Sample images
```

## Technical Implementation

### 1. Human Segmentation

- Uses DeepLabV3+ with ResNet backbone for accurate human segmentation
- Identifies clothing regions specifically to target for replacement
- Preserves body/skin areas during processing

### 2. Virtual Try-On

- Implements Stable Diffusion inpainting for realistic clothing synthesis
- Falls back to VITON-based approach if diffusion models unavailable
- Maintains consistency in lighting and shadows

### 3. Image Processing

- Preserves facial features from original image
- Maintains consistent skin tone between original and modified images
- Applies realistic lighting and shadow effects
- Uses Poisson blending for seamless integration

### 4. Realism Enhancement

- Adds realistic shadows based on human silhouette
- Adjusts lighting for natural appearance
- Blends clothing edges seamlessly with body

## For College Mini Project

This project demonstrates several advanced AI/ML concepts:

1. **Computer Vision**: Object detection, segmentation, and image manipulation
2. **Generative Models**: Stable Diffusion for image synthesis
3. **Deep Learning**: Neural networks for image processing
4. **User Interface**: Web-based interface for practical application

### Learning Outcomes

- Understanding of semantic segmentation
- Experience with diffusion models
- Knowledge of image processing techniques
- Practical implementation of AI applications

## Testing

To test the complete pipeline:

1. Prepare sample images:

   - A clear front-facing photo of a person
   - An image of the desired clothing item

2. Run the application and upload the images

3. Observe that:
   - Face features are preserved
   - Body pose remains unchanged
   - Skin tone is consistent
   - Only clothes are replaced realistically

## Limitations

- Works best with front-facing person images
- Quality depends on image resolution and lighting
- May struggle with complex poses or occlusions
- Processing time varies based on hardware (faster with GPU)

## Future Improvements

- Support for multiple people in images
- Real-time processing capabilities
- Better pose alignment for different body positions
- Enhanced cloth physics simulation

## Troubleshooting

If you encounter issues:

1. Ensure all dependencies are installed correctly
2. Check that your images are in JPG/PNG format
3. Verify images are not corrupted
4. Make sure you have sufficient disk space for model downloads
5. For CUDA-related issues, try running on CPU by modifying device settings

## License

This project is created for educational purposes as a college mini-project.

---

**Note**: This project is designed for academic purposes and demonstrates the concepts of AI-powered virtual try-on technology.
