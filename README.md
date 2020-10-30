# lazydep
Lazily evaluate function dependency graph

There's pretty much 1 function that is worth noting:

```python
lazydep.resolve(graph, state, functions, request=None)
```


Evaluates some set of functions, according to tome dependency graph structure

	Arguments:
			graph: dictionary, mapping function names to the names of parameters required for their execution
			state: dictionary, initial input to functions. the remainder of intermediary parameters will be bootstrapped
			functions: list of functions in any order, or dictionary mapping function names to functions
			request: name of desired function evaluation. If request is specified, only the desired function call will be returned. If left empty, all functions specified will be returned, in the same form as state object.

	Returns:
			dictionary, or result of 'request' function
