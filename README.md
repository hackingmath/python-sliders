# python-sliders
Sliders for the Python mode of Processing

<p>If you use the Python mode for Processing, now you can add sliders to your sketch to change variable values dynamically. Simply put slider.py into the same folder as your sketch and import the Slider class at the top:</p>
<code>from slider import Slider</code>
<p>Outside the setup function, create the slider object by giving it a range (here it's 0 to 20) and a default value for when it first runs (in this case, 6):</p>
<code>slider1 = Slider(0,20,6)</code>
<p>Inside the setup function, give the slider a position:</p>
<code>slider1.position(20,20)</code>
<p>In the draw function, assign the value of the slider to a variable:</p>
<code>num = slider1.value()</code>
<p>You have the option of labeling the slider, too:</p>
<code>slider1.label = "number"</code>
<p>I've included a couple of example files to show how it works in action. Have fun and let me know how you like it!</p>
