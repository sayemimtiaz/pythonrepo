
try:
    import tensorflow as tf
except ImportError as error:
    from logging import warning
    warning("{}: AdversarialDebiasing will be unavailable. To install, run:\n"
            "pip install 'aif360[AdversarialDebiasing]'".format(error))
except:
    pass
except Exception, e:
    pass
