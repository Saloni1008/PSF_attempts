# PSF_attempts
Attempts made on PSF extraction by running optimizations on the data image of MG2016+112

1. Running an optimization on the complete mass+light profile model in glafic
2. Running an optimization on the same model using fmin but only using the point source images' regions (A & B) for optimizing
3. Running an mcmc optimization on the model using the entire data image
4. Running an optimization on the same model using fmin but using the entire data image
5. Running an mcmc optimization on the model using only the point source images' regions (A & B) for optimizing
6. Running an optimization in glafic for the light profile using only the point source images' regions (A & B) and lens D for optimizing
7. Running an optimization using fmin for the light profile using only the point source images' regions (A & B) and lens D for optimizing
8. Noise subtraction done from the data image and use of A and B as PSF individually (Use of one image as the PSF is not found to be satisfactory. While one of the image inevitably fits, the other shows a slight offset)

The directory 'residuals' contains the residuals for each of the above attempts. 
