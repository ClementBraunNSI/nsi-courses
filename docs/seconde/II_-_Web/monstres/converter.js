const fs = require('fs');
const path = require('path');
const sharp = require('sharp');

// Supported input formats
const SUPPORTED_FORMATS = ['.png', '.jpg', '.jpeg'];

// Function to convert image to WebP
async function convertToWebP(inputPath) {
    try {
        const ext = path.extname(inputPath);
        if (!SUPPORTED_FORMATS.includes(ext.toLowerCase())) {
            console.error(`Unsupported file format: ${ext}`);
            return;
        }

        const outputPath = inputPath.replace(ext, '.webp');
        
        await sharp(inputPath)
            .webp({ quality: 80 }) // 80% quality for good balance
            .toFile(outputPath);

        console.log(`Successfully converted: ${path.basename(inputPath)} -> ${path.basename(outputPath)}`);
    } catch (error) {
        console.error(`Error converting ${inputPath}:`, error);
    }
}

// Function to process a directory
async function processDirectory(directoryPath) {
    try {
        const files = fs.readdirSync(directoryPath);
        
        for (const file of files) {
            const filePath = path.join(directoryPath, file);
            const stat = fs.statSync(filePath);
            
            if (stat.isDirectory()) {
                await processDirectory(filePath); // Process subdirectories recursively
            } else if (SUPPORTED_FORMATS.includes(path.extname(file).toLowerCase())) {
                await convertToWebP(filePath);
            }
        }
    } catch (error) {
        console.error('Error processing directory:', error);
    }
}

// Example usage
const targetPath = ''; // Change this to your images directory
let liste = ['./2DE1','./2DE10/','./2DE11/','./2DE2/','./2DE3/','./2DE5/','./2DE6/','./2DE7/','./2DE9/','S01','S16','S18']
for (let i = 0; i < liste.length; i++) {
    targetPath = liste[i]
    processDirectory(targetPath);
}
