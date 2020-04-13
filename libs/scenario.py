from functools import wraps


def _inherited_args(args, kwargs, tc_kwargs):
    inherited_kwargs = {}
    for param_name, value in tc_kwargs.items():
        if param_name in kwargs or param_name in args:
            inherited_kwargs[param_name] = value
    
    return inherited_kwargs


def starting_scenario(func, *args, **kwargs):
    def wrapper(tc):
        @wraps(tc)
        def tc_wrapper(*tc_args, **tc_kwargs):
            if func:
                inherited_kwargs = _inherited_args(args, kwargs, tc_kwargs)
                func(**{**kwargs, **inherited_kwargs})

            tc(*tc_args, **tc_kwargs)
        return tc_wrapper
    return wrapper
