# class
# =======================================
class Exceptions:

    # load
    from klibee.exceptions.cannot_cast_metadata    import CannotCastMetadataException
    from klibee.exceptions.cannot_connect_to_redis import CannotConnectRedisException
    from klibee.exceptions.cannot_download_file    import CannotDownloadFileException
    from klibee.exceptions.empty_results           import EmptyResultsException
    from klibee.exceptions.no_metadata_in_redis    import NoMetadataInRedisException