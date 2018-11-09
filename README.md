Layers and Organization
-----------------------
The common depiction of clean architecture is a diagram consisting of concentric circular layers, very reminiscent of the onion architecture, which is not a surprise. The idea here is that the inner layers are high-level, abstract policies; the outer layers are technical implementation details.

The proposed layers are

* **Entities:** Here should live the business objects of your application, generally called “entities,” in DDD lingo.
* **Use cases:**. In this layer reside the use cases; in short, we could say that these are objects that represent an action a user can perform in the application.
* **Interface adapters:** This layer contains code whose goal is basically to provide a bridge between the outside world and the immaculate world inhabited by the use cases and entities. Models, views, presenters, and repository implementations all should go here.
* **Frameworks and drivers:** Finally, we have the layer that basically represents external agents: the web, the database, etc.

The Dependency Rule
-------------------
The aforementioned layer organization isn’t set in stone, though. There’s nothing really stopping you from using more than that if you need to. What you really have to remember is to follow the dependency rule: all dependencies should point inwards.

The entities layer shouldn’t be aware of any other layer in the application. There should be no change in the outer layers that causes a change to it. The opposite holds, though: a change in the entities layer can and probably will cause changes in next layers.