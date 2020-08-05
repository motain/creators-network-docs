OneFootball Network API
=======================

Introduction
------------

| OneFootball is the world's leading digital football platform. The OneFootball Network API allows OneFootball's content partners to publish articles onto the OneFootball platform. It also allows partners to update and delete articles that they have already published to the OneFootball platform.


| The API can be used by partners to set up their own services such that content published on their sites is automatically sent to OneFootball and natively integrated onto the OneFootball platform for OneFootball users.


| Please note that the OneFootball Network is a closed, invite-only platform and only authorized content partners are able to use the OneFootball Network API.


Conventions
-----------

| Before you get started, please note the conventions listed here, which apply throughout the API.


Schema
~~~~~~

| All API access is over HTTPS. All data is sent and received in JSON format.

| Access is from the following URL: https://network-api.onefootball.com


Time format
~~~~~~~~~~~

| All timestamps return in ISO 8601 format ``YYYY-MM-DDTHH:MM:SSZ``.

Authentication
~~~~~~~~~~~~~~

| Requests that require authentication must provide ``Authorization`` header. The value must be a ``Bearer`` token acquired during the login process.

Examples
~~~~~~~~

| In the documentation, we have tried to give code snippet examples that can be copied, pasted and adjusted rather than describing everything in words. Please look to the examples as a reference.

Testing
~~~~~~~

| When testing the publication and updating of articles, use the optional ``draft`` boolean. A request sent with ``draft`` being ``TRUE`` will ensure that the respective article *will not* be visible to OneFootball users.

| When you are ready to use your service in production and send real articles to be seen by OneFootball users, you can either leave out the ``draft`` parameter or set ``draft`` to ``FALSE``.

|

Getting set up
--------------

| In order to publish, update or delete content on OneFootball via the OneFootball Network API, you must first do the following:

1. Complete the registration for your OneFootball Network account.
2. Use your login credentials to retrieve an authentication token that must be used for other requests.


Activating your OneFootball Network account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The OneFootball Network in an invitation-only platform. If you are invited to join and have agreed to come onboard, you will receive a registration email. Please follow the instructions in the registration email, set your password and then proceed to log in to the OneFootball Network portal. Make sure to complete the onboarding process in the portal before trying to publish content via the OneFootball Network API.


Retrieving an authentication token
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Once you have successfully logged in to the OneFootball Network portal, you can use the same email address and password credentials to obtain an authentication token for the OneFootball Network API.

| You must have a valid authentication token in order to publish, modify, or delete content via requests made to the OneFootball Network API. To acquire a token, send your login credentials as per the example below:


.. example-code::

   .. code-block:: shell

      $ curl -X POST \
          https://network-api.onefootball.com/v1/login \
          -H "Content-Type: application/json" \
          -d '{"login": "EMAIL_ADDRESS", "password": "SECRET_PASSWORD"}'

   .. code-block:: python

      import requests

      headers = {
          'Content-Type': 'application/json',
      }

      data = {"login": "EMAIL_ADDRESS", "password": "SECRET_PASSWORD"}

      response = requests.post(
          'https://network-api.onefootball.com/v1/login',
          headers=headers,
          data=data
      )

   .. code-block:: go

      type Payload struct {
       Login    string `json:"login"`
       Password string `json:"password"`
      }

      data := Payload{
      // fill struct
      }
      payloadBytes, err := json.Marshal(data)
      if err != nil {
       // handle err
      }
      body := bytes.NewReader(payloadBytes)

      req, err := http.NewRequest("POST", "https://network-api.onefootball.com/v1/login", body)
      if err != nil {
       // handle err
      }
      req.Header.Set("Content-Type", "application/json")

      resp, err := http.DefaultClient.Do(req)
      if err != nil {
       // handle err
      }
      defer resp.Body.Close()


Refreshing an authentication token
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Each authentication token is valid for seven days after it is issued. After a token expires, repeat the process by using your login credentials to acquire a new one.


Publishing content
------------------

| Once you are set up and have an authentication token, you can publish an article to OneFootball.


Publishing an article
~~~~~~~~~~~~~~~~~~~~~

| Using a valid authentication token, you can publish an article by sending a ``POST`` request to the posts entity endpoint.

| To do so, take the example below and do the following:

* Replace ``TOKEN`` in the header with your valid authentication token.
* Set all article attributes as shown in the example below.

.. example-code::

   .. code-block:: shell

      $ curl -X POST \
          https://network-api.onefootball.com/v1/posts/ \
          -H "Content-Type: application/json" \
          -H 'Authorization: Bearer TOKEN' \
          -d '{
              "external_id": "ARTICLE_ID",
              "source_url": "ARTICLE_URL",
              "language": "en",
              "published": "2010-01-02T15:04:05Z",
              "modified": "2010-01-02T15:04:05Z",
              "content": "Article content",
              "title": "Article title",
              "image_url": "https://your-blog.com/images/1.png",
              "image_width": 200,
              "image_height": 100,
              "draft": false
          }'

   .. code-block:: python

      import requests

      headers = {
          'Authorization': 'Bearer TOKEN',
      }

      data = {
          "external_id": "ARTICLE_ID",
          "source_url": "ARTICLE_URL",
          "language": "en",
          "published": "2010-01-02T15:04:05Z",
          "modified": "2010-01-02T15:04:05Z",
          "content": "Article content",
          "title": "Article title"
          "image_url": "https://your-blog.com/images/1.png",
          "image_width": 200,
          "image_height": 100,
          "draft": false
      }

      response = requests.post(
        'https://network-api.onefootball.com/v1/posts/',
        headers=headers,
        data=data
      )


   .. code-block:: go

      type Payload struct {
       ExternalID         string    `json:"external_id"`
       SourceURL          string    `json:"source_url"`
       Language           string    `json:"language"`
       Published          time.Time `json:"published"`
       Modified           time.Time `json:"modified"`
       Content            string    `json:"content"`
       Title              string    `json:"title"`
       ImageURL           string    `json:"image_url"`
       ImageWidth         int       `json:"image_width"`
       ImageHeight        int       `json:"image_height"`
       Draft              bool      `json:"draft"`
      }

      data := Payload{
      // fill struct
      }
      payloadBytes, err := json.Marshal(data)
      if err != nil {
       // handle err
      }
      body := bytes.NewReader(payloadBytes)

      req, err := http.NewRequest("POST", "https://network-api.onefootball.com/v1/posts/", body)
      if err != nil {
       // handle err
      }
      req.Header.Set("Content-Type", "application/json")
      req.Header.Set("Authorization", "Bearer TOKEN")

      resp, err := http.DefaultClient.Do(req)
      if err != nil {
       // handle err
      }
      defer resp.Body.Close()


+--------------------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field              | Usage      | Description                                                                                                                                                                                                                                   |
+====================+============+===============================================================================================================================================================================================================================================+
| ``external_id``    | required   | The ID of the article as defined in your system. It must be unique (within a given language) within your own system.                                                                                                                          |
+--------------------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``source_url``     | required   | The link to the article as published on your website. Place your homepage url if the article is not published anywhere else.                                                                                                                  |
+--------------------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``language``       | required   | The language of the article. Valid choices are ``en``, ``de``, ``es``, ``fr``, ``br``, and ``it``.                                                                                                                                            |
+--------------------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``published``      | required   | The time that the article was published. If in doubt, use the current time.                                                                                                                                                                   |
+--------------------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``modified``       | required   | The time that the article was last updated. If in doubt, use the current time.                                                                                                                                                                |
+--------------------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``content``        | required   | The content of the article, which must be in correctly-formatted HTML. Please see `this link <https://static.onefootball.com/onefootball-network/technical-documentation/html-guidelines>`_ for important details on acceptable HTML content. |
+--------------------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``title``          | required   | The title of the article. The title cannot be an empty string.                                                                                                                                                                                |
+--------------------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``image_url``      | optional   | An optional field for the URL of the article's featured image. If provided, ``image_width`` and ``image_height`` should be provided as well (the image's width and height in pixels).                                                         |
+--------------------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``draft``          | optional   | An optional boolean to be used for testing purposes. If set to ``true``, the article will not be made visible to OneFootball users. If not povided, the article will by default be made available to OneFootball users.                       |
+--------------------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

|

Updating and deleting content
-----------------------------

| Once your content is on OneFootball, you can manage your content by updating and deleting it.

| In order to update or delete an article on OneFootball, you will first need to get the OneFootball post ID for that article.


Obtaining an article's post ID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| To get the OneFootball post ID for an article so that you can reference it in update or delete operations, take the example below and do the following:

* Replace ``EXTERNAL_ID`` in the URL with the id of the article in your system that you provided when publishing the article. This should be encoded if necessary.
* Replace ``TOKEN`` in the header with your valid authentication token.


.. example-code::

   .. code-block:: shell

      $ curl -X GET \
          https://network-api.onefootball.com/v1/posts/?external_id=EXTERNAL_ID \
          -H "Content-Type: application/json" \
          -H 'Authorization: Bearer TOKEN'

   .. code-block:: python

        import requests

        headers = {
            'Authorization': 'Bearer TOKEN',
        }

        params = {
            'external_id': 'EXTERNAL_ID',
        }

        response = requests.get(
            'https://network-api.onefootball.com/v1/posts/',
            headers=headers,
            params=params
        )

   .. code-block:: go

      req, err := http.NewRequest("GET", "https://network-api.onefootball.com/v1/posts/?external_id=EXTERNAL_ID", nil)
      if err != nil {
       // handle err
      }
      req.Header.Set("Content-Type", "application/json")
      req.Header.Set("Authorization", "Bearer TOKEN")

      resp, err := http.DefaultClient.Do(req)
      if err != nil {
       // handle err
      }
      defer resp.Body.Close()



Updating an article
~~~~~~~~~~~~~~~~~~~

| Occasionally, you may edit an article from your site. To ensure that this article is updated on OneFootball, use the ``PUT`` method of the post entity endpoint.

| To do so, take the example below and do the following:

* Replace ``POST_ID`` in the URL with the OneFootball post ID of the article you want to update (see above for how to obtain this).
* Replace ``TOKEN`` in the header with your valid authentication token.
* Set all article attributes as shown in the example below. Note that all attributes will overwrite existing values.

.. example-code::

   .. code-block:: shell

      $ curl -X PUT \
          https://network-api.onefootball.com/v1/posts/POST_ID \
          -H "Content-Type: application/json" \
          -H 'Authorization: Bearer TOKEN' \
          -d '{
              "source_url": "ARTICLE_URL",
              "language":  "en",
              "published": "2010-01-02T15:04:05Z",
              "modified": "2010-01-02T15:04:05Z",
              "content":  "Article content",
              "title":  "Article title",
              "image_url":  "https://your-blog.com/images/1.png",
              "image_width":  200,
              "image_height":  100,
              "draft": false
          }'

   .. code-block:: python

        import requests

        headers = {
            'Authorization': 'Bearer TOKEN',
        }

        data = {
            "source_url": "ARTICLE_URL",
            "language":  "en",
            "published": "2010-01-02T15:04:05Z",
            "modified": "2010-01-02T15:04:05Z",
            "content":  "Article content",
            "title":  "Article title"
            "image_url":  "https://your-blog.com/images/1.png",
            "image_width":  200,
            "image_height":  100,
            "draft": false
        }

        response = requests.put(
            'https://network-api.onefootball.com/v1/posts/POST_ID',
            headers=headers,
            data=data
        )

   .. code-block:: go

      type Payload struct {
       SourceURL          string    `json:"source_url"`
       Language           string    `json:"language"`
       Published          time.Time `json:"published"`
       Modified           time.Time `json:"modified"`
       Content            string    `json:"content"`
       Title              string    `json:"title"`
       ImageURL           string    `json:"image_url"`
       ImageWidth         int       `json:"image_width"`
       ImageHeight        int       `json:"image_height"`
       Draft              bool      `json:"draft"`
      }

      data := Payload{
      // fill struct
      }
      payloadBytes, err := json.Marshal(data)
      if err != nil {
       // handle err
      }
      body := bytes.NewReader(payloadBytes)

      req, err := http.NewRequest("PUT", "https://network-api.onefootball.com/v1/posts/POST_ID", body)
      if err != nil {
       // handle err
      }
      req.Header.Set("Content-Type", "application/json")
      req.Header.Set("Authorization", "Bearer TOKEN")

      resp, err := http.DefaultClient.Do(req)
      if err != nil {
       // handle err
      }
      defer resp.Body.Close()


+--------------------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field              | Usage      | Description                                                                                                                                                                                                                                   |
+--------------------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``source_url``     | required   | The link to the article as published on your website. Place your homepage url if the article is not published anywhere else.                                                                                                                  |
+--------------------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``language``       | required   | The language of the article. Valid choices are ``en``, ``de``, ``es``, ``fr``, ``br``, and ``it``.                                                                                                                                            |
+--------------------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``published``      | required   | The time that the article was published. If in doubt, use the current time.                                                                                                                                                                   |
+--------------------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``modified``       | required   | The time that the article was last updated. If in doubt, use the current time.                                                                                                                                                                |
+--------------------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``content``        | required   | The content of the article, which must be in correctly-formatted HTML. Please see `this link <https://static.onefootball.com/onefootball-network/technical-documentation/html-guidelines>`_ for important details on acceptable HTML content. |
+--------------------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``title``          | required   | The title of the article. The title cannot be an empty string.                                                                                                                                                                                |
+--------------------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``image_url``      | optional   | An optional field for the URL of the article's featured image. If provided, ``image_width`` and ``image_height`` should be provided as well (the image's width and height in pixels).                                                         |
+--------------------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``draft``          | optional   | An optional boolean to be used for testing purposes. If set to ``true``, the article will not be made visible to OneFootball users. If not povided, the article will by default be made available to OneFootball users.                       |
+--------------------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


Deleting an article
~~~~~~~~~~~~~~~~~~~

| You can also delete articles from OneFootball using the ``DELETE`` method of the posts endpoint.

| To do so, take the example below and do the following:

* Replace ``POST_ID`` in the URL with the OneFootball post ID of the article you want to delete (see above for how to obtain this)
* Replace ``TOKEN`` in the header with your valid authentication token.

.. example-code::

   .. code-block:: shell

      $ curl -X DELETE \
          https://network-api.onefootball.com/v1/posts/POST_ID \
          -H "Content-Type: application/json" \
          -H 'Authorization: Bearer TOKEN'

   .. code-block:: python

        import requests

        headers = {
            'Authorization': 'Bearer TOKEN',
        }

        response = requests.delete(
            'https://network-api.onefootball.com/v1/posts/POST_ID',
            headers=headers
        )

   .. code-block:: go

      req, err := http.NewRequest("DELETE", "https://network-api.onefootball.com/v1/posts/POST_ID", nil)
      if err != nil {
       // handle err
      }
      req.Header.Set("Content-Type", "application/json")
      req.Header.Set("Authorization", "Bearer TOKEN")

      resp, err := http.DefaultClient.Do(req)
      if err != nil {
       // handle err
      }
      defer resp.Body.Close()
