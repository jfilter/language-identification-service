import urllib
from collections import Counter

import responder
from pyfasttext import FastText

# download model every time
testfile = urllib.request.URLopener()
testfile.retrieve(
    "https://s3-us-west-1.amazonaws.com/fasttext-vectors/supervised_models/lid.176.ftz", "lid.176.ftz")
model = FastText('lid.176.ftz')

api = responder.API()


def is_german(data):
    texts = data.get_list('text')
    preds = sum(predict_lang(texts), [])
    # check if the most common is german
    return Counter(preds).most_common(1)[0][0] == 'de'


def predict_lang(texts):
    return model.predict(texts)


@api.route("/german")
async def german(req, resp):
    resp.media = {"isGerman": is_german(await req.media())}

if __name__ == '__main__':
    api.run()
