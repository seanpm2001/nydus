"""
nydus.db.base
~~~~~~~~~~~~~

:copyright: (c) 2011 DISQUS.
:license: Apache License 2.0, see LICENSE for more details.
"""


__all__ = ('BaseRouter',)


class BaseRouter(object):
    """
    Handles routing requests to a specific connection in a single cluster.
    """
    retryable = False

    def get_db(self, cluster, func, *args, **kwargs):
        """
        Return the first entry in the cluster
        The return value must be iterable
        """
        return range(len(cluster))
