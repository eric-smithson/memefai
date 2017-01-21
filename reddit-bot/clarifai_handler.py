# this where we will build the functions which handle all our clarifai interactions

# should pass in an image and return a list of tags
def get_tags(image_url):
    # Acces Token gFISSpi0OPDjRVXc5K4nfUYgJ0S5Bz
    # Pip install the client:
    # pip install clarifai
    #

    # The package will be accessible by importing clarifai:

    from clarifai import rest
    from clarifai.rest import ClarifaiApp

    # The client takes the `APP_ID` and `APP_SECRET` you created in your <a href="/account/application">Clarifai
    # account.</a> You can set these variables in your environment as:

    # - `CLARIFAI_APP_ID`
    # - `CLARIFAI_APP_SECRET`

    from clarifai.rest import ClarifaiApp

    #This is our actual ID and pass
    app = ClarifaiApp("HdVa7-OQfNKRsMiWPXeby4Ik5bMiQ7DtK8i74VsU", "aAdmMpsV6GK9M7G-vMzDo49lWVZ4SkqGm6kApiW0")

    # getting the general model
    model = app.models.get("general-v1.3")

    # predicts with the above model (general)
    tags_raw = model.predict_by_url(url = image_url)

    tag_dicts = tags_raw['outputs'][0]['data']['concepts']
    tags_clean = [str(d['name']) for d in tag_dicts]

    #this would be a list of tags
    return (tags_clean)


