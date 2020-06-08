## START CODE HERE ## (PUT YOUR IMAGE NAME) 
import imageio
import scipy
my_image = "my_image.jpg"   # change this to the name of your image file 
## END CODE HERE ##
print(55)

# We preprocess the image to fit your algorithm.
fname = r"E:\Neural Networks and Deep Learning\images\my_image.jpg"
image = np.array(imageio.imread(fname))
image = image/255.
my_image = scipy.misc.imresize(image, size=(num_px,num_px)).reshape((1, num_px*num_px*3)).T
my_predicted_image = predict(d["w"], d["b"], my_image)

plt.imshow(image)
print("y = " + str(np.squeeze(my_predicted_image)) + ", your algorithm predicts a \"" + classes[int(np.squeeze(my_predicted_image)),].decode("utf-8") +  "\" picture.")