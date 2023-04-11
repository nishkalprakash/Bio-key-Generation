# Fingerprint Key Generation Process
* Preprocessing
  * Vertically Align image
  * Enhance image
* Consistent Region Selection (CRS)
  * Selecting the region of interest (ROI) based on GLCM statistical feature descriptors
* Hybrid Feature Extraction - [Indirect Features (1024 bits), Texture feature 1 (hcbd || gcbd || ltp) (1024 bits), Texture feature 2 (1536 bits) (hcbd || gcbd || ltp || mtp)] 
  * Minutia Feature Extraction using Delaunay Triangulation (Indirect Features) (1024 bits)
    ```
    Indirect Feature Vector (Fv ) = 
    [
      r_area(∀△ ∈TR) ∥
      r_length_of_sides(∀△i ∈TR) ∥
      r_angles_b/w_sides(∀△ ∈ TR) ∥
      r_incenter(∀△ ∈ TR) ∥
      r_position(∀ mi ∈ m) ∥
      r_orientation(∀ mi ∈ m)
    ]
    ```
  * Minutia Feature Extraction using Hough Transform (Direct Features)
  * Minutia Feature Extraction using Gabor Filter (Direct Features)
  * Texture Feature Extraction HCBD (256 bits), GCBD (256 bits), LTP (512 bits) and MTP (512 bits)
    * Hilbert curve-based descriptor (HCBD)
    * Gray code-based descriptor (GCBD)
    * Local ternary pattern (LTP)
    * Median ternary pattern (MTP)
* Prominent Feature Selection
  * Feature Selection using Genetic Algorithm
* Discriminant Feature Vector Generation
  * Metric learning based discriminant feature vector
    * Information Theoretic Metric Learning (ITML) technique
* Stable Key Generation