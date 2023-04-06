__all__ = ['Milvus', 'Faiss']

from gptcache.utils.lazy_import import LazyImport

milvus = LazyImport('milvus', globals(), 'gptcache.manager.vector_data.milvus')
faiss = LazyImport('faiss', globals(), 'gptcache.manager.vector_data.faiss')


def Milvus(**kwargs):
    return milvus.Milvus(**kwargs)


def Faiss(index_file_path, dimension, top_k, skip_file=False):
    return faiss.Faiss(index_file_path, dimension, top_k, skip_file)
