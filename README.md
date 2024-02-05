# Using pywaterflood and Docker

[Pywaterflood](https://pywaterflood.readthedocs.io) allows you to perform capacitance resistance modeling on some very large reservoirs. It has been tested on up to several years of data for a field with 600 wells. At that point, though, it makes sense to use a [supercomputer](https://tacc.utexas.edu/) or cloud computation. And for those, [containers](https://tacc.utexas.edu/news/latest-news/2020/02/19/supporting-portable-reproducible-computational-science/) might be the tool of choice. Here is an example project using Docker with pywaterflood.

To run this example, call

```
docker compose up
```

You can then copy the results out of the Docker volume with

```
docker run --rm -v docker-pywaterflood_results:/src -v $(pwd)/results:/dest alpine sh -c 'cp -R /src/* /dest/'
```

After that, you can start analyzing the results in your new `results` folder.

To modify this to your needs, you might want to

1. Change the data in the `data` folder to match your production and injection data
1. Use different settings inside of run_crm.py
