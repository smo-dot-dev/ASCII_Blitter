# ASCII_Blitter
Convert any image into an ASCII image of the same size, with a simple Python script!

Will output to the console, and also generates `output.html` with colors

# How to make it work
Make sure you install PIL:

`pip install Pillow`

Set the variables correctly:

`DOWNSCALE_FACTOR = 4` - Make it match the fontsize if you want the output to be of the same size as the input.

`RGB_AS_BACKGROUND = True` - If false, will set the text foreground color and white background, otherwise uses px color as bg

`FORCE_SQUARE = True` - Enable when using regular fonts (rectangular) so will print horizontal chars twice to preserve original aspect ratio. Disable when using square sprites.

and set the image path, accepts .png, .jpg, .gif...

`image_path = "Untitled.png"`

# Example
Input example: 

![](Untitled.png)


HTML Output screenshot (FORCE_SQUARE=True, DS_FACTOR 4, RGB_AS_BG=True)

![](1.png)




Text Output (FORCE_SQUARE=True, DS_FACTOR 10, RGB_AS_BG=True)
```
==~~,,,,****************++~~~~++++~~~~++++----++~~++++++++----------****,,,,,,,,
;;++,,****----**************,,**--++====~~~~++++--****,,,,,,,,,,,,,,,,**,,,,,,**
~~--****----**************----++~~==~~==~~++----**------------------**,,,,,,****
--------------------******----~~============--****,,**--------------**,,,,******
--------------**----**--******++;;vvvveeddttee==--,,****************--**********
------------------------------++eeddmmmmssssmmtt~~**********************--******
++----------------------------~~ooss######ssmmtt~~********----------------------
++++++++++++++------++++++++++;;mmss######ssmmtt~~------------------------------
++++++++++++++--------++++--==ddmmmmmmssssssmmdd~~----------------++----++++++++
==++++++==eeddddeeddeeeeeeeeddssssmmooddmmoovv~~++++==eeeevv;;==~~~~~~~~~~~~~~~~
;;++++++eeddoossmmmmssmmmmmmoossssssmmoossoovvdd~~++eeddddoo;;vv;;~~~~~~~~~~~~~~
;;~~~~++ttooeeddttddttttddttttmmssss##ss##dd;;ddee++vveeddoo~~~~~~~~~~~~~~~~~~~~
==~~~~~~ttooeeeeeeeeeeeeeeeeeeeettss##ss##dd==ooee==eevveeoo==~~~~~~~~~~~~~~~~~~
====~~~~ddooddeeddddeeddddddee++;;ssssssssoo++;;==--vveeddtt========~~~~==~~~~==
======~~ddddddddddddddeevv;;~~++==oossmmmmoo~~++--,,--;;eett====================
========eeddeeddeevv;;====~~++====oommssmmooee;;**,,,,,,--~~~~==================
;;====~~eeddddee======~~==++~~====ddddssmmoott~~,,,,,,,,,,,,**--++==============
==++++++;;ddee;;~~======~~--======oooooooooo;;--**,,,,,,,,**++++**++============
;;++++++==ddee;;========++--~~====ddssoooovv==++**,,,,,,,,++++++**--~~~~~~~~~~~~
vv======;;dddd;;======~~--++======oooommddddddvv**,,,,,,**~~++++,,++========~~==
ee;;;;==;;oott;;======~~--++======ddddooooddmmoo**,,,,,,**~~++--,,++;;;;;;==;;;;
ee;;;;====oott;;======++--++======ttddeemmdddd;;,,,,**--~~~~--**,,--;;;;;;==;;;;
ee;;;;==;;oodd====~~~~++**++====~~eettvvttvv==**,,----~~==++--,,,,**;;==;;;;;;;;
ee;;;;==;;oodd====~~~~++**++==~~~~eemmmmttddee--++++--~~==--**,,,,**==;;;;;;;;;;
ee;;;;;;vvooee====~~~~++**~~~~~~~~;;ssss##mmvv++++++--~~~~****--**,,++;;;;;;;;;;
vv;;==;;vvooee====++**++**--++++~~;;mmssmmtt;;++++++--~~++,,----****--;;;;;;;;;;
vv;;;;;;eeoovv====~~------**--++++==mmmmttddee++++--++~~**,,--++--****;;;;;;;;;;
vv;;;;vveeoo;;======~~++--**----++~~mmooddssvv++~~**----,,**++~~--,,,,==;;;;====
;;;;vvvveeoo;;======++--****------~~mmssssss;;~~++,,--**,,++~~~~**,,**~~;;;;====
;;;;vvvvddoovv======--******--++**~~mm##ssoo;;~~**,,**,,**++~~++**----~~========
;;vveeeeddoovv====~~----****----**--;;ddttvv==++,,,,,,,,--++~~++--++**~~========
vveeeeeettoo======~~--**,,,,,,,,****~~oooott;;--,,,,,,,,--~~~~++--**,,++;;======
eeeeddeettdd======++**,,,,,,,,------==oossmmee,,,,,,,,,,**++++--********========
ddddddddttoo======~~--****,,**~~++--==ddddoovv,,,,,,,,,,**++++++++--**--========
eeeeeeddddoo~~~~++--**--**,,--~~--~~ttss####dd..,,,,,,,,,,--~~++--****~~========
eeeeeeeeddoo~~~~~~--****,,,,**++--++ttddttddee~~,,,,,,,,,,--++------,,--==;;====
vveeeeeeddoo======++--,,,,,,**--==ttoooooommmmoovv**,,******--++++**,,**vvvv;;==
eeeeeeeeddoo======~~~~--,,,,**,,;;ttddttddee==----******,,--++++++**,,--;;vv;;==
eeeeeeeeddoo;;~~======~~**,,,,,,--------******,,****----**--++++--**,,++==;;;;==
eeeeeeeettooee~~========++,,,,**++~~++++----****------++--++~~++--****~~====;;==
```


