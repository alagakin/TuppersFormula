from PIL import Image, ImageDraw
const = 4858408935162463366908076825970252427173967932720072864441539000012226501005956349247659903249882787055844485041606368176077263420666238397958573888226570402520730213452508485401922500067251176226210382373843800207071465276852864207225857233993905609312869794955766719328662732949846100776164031291897946260086772420627056770772091384200518623774781595361252252831419037611269415154337255729437905580391370620968436102889370310847256046341477493168075800438128104453948486957478473013863842808971844083478460095527003833238650729267993935609822
image = Image.new("1", (106, 17), (0))
for i in range(0, 17):
    for j in range(0, 106):
        result = (((const + i) // 17) // (2 ** (17 * j + ((const + i) % 17)))) % 2
        image.putpixel((105 - j, i), (0)) if result != 0 else image.putpixel((105 - j, i), (255))
image.save("image.png")