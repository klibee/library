# class
# =======================================
class Exceptions:

    # common
    from klibee.exceptions.common.cannot_cast_metadata    import CannotCastMetadataException
    from klibee.exceptions.common.empty_results           import EmptyResultsException

    # files
    from klibee.exceptions.files.cannot_download_file     import CannotDownloadFileException

    # redis
    from klibee.exceptions.redis.cannot_connect_to_redis  import CannotConnectRedisException
    from klibee.exceptions.redis.no_metadata_in_redis     import NoMetadataInRedisException