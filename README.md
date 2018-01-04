# Signal-Cross-Correlation

An exercise in Signal Processing to demonstrate how the equation for cross-correlation (https://en.wikipedia.org/wiki/Cross-correlation) can be used to recognize a facsimile of a one-dimensional signal regardless of whether it is distorted by noise or translated. Using MatPlotLib to graph, an interface shows the x-coordinate on the after-image at which both graphs share the point of highest correlation and the point of lowest correlation according to the equation used.
\\
Here is a random output by the script: The pre-image signal towards the top. The bottom half contains the image that has been shifted over by a random amount and distorted using a normal distribution. Of course, the interesting part is that the simple equation shown is able to recognize where they both 'line up' flawlessly, and it can be observed in that the point at which there is the highest correlation corresponds the the zero-coordinate of the pre-image signal.






![selection_001](https://user-images.githubusercontent.com/14042582/34587603-98519406-f16e-11e7-8265-46ee3e691db5.png)
