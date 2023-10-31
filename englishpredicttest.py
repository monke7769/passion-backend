from aienglishprediction import aienglishprediction
from caesar import caesar
pred=aienglishprediction()
pred.predict("/...././........................................................................")
pred.predict("bro this shit aint working im getting mad")

for i in range(1,27):
    cease=caesar(0,"Y belu je setu ie cksx rusqkiu yj yi luho vkd qdt jxyi yi co cuiiqwu")
    print(cease.decrypt(i),"thing")
    if(pred.predict(cease.decrypt(i))==0):
        value=cease.decrypt(i)
    print(i)
print(value)