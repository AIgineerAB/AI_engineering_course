# Creating a package

In Python you need to create a package in order to simplify importing modules from different folders. Without packaging you can only import from sibling and children directories, but not children of a sibling directory for example. To create a package using uv you run this command:  

```bash
uv init --package <name>
```

Watch this video to learn about packaging

<a href="https://youtu.be/ISBgzg533GQ" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/machine_learning/packaging.png?raw=true" alt="packaging with uv" width="600">
</a>