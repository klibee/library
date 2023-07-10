# class
# =======================================
class Exceptions:

    # common
    from klibee.exceptions.common.cannot_cast_metadata    import CannotCastMetadataException
    from klibee.exceptions.common.empty_results           import EmptyResultsException

    # files
    from klibee.exceptions.files.cannot_download_file     import CannotDownloadFileException
    from klibee.exceptions.files.file_does_not_exists     import FileDoestNotExistsException

    # redis
    from klibee.exceptions.redis.cannot_connect_to_redis  import CannotConnectRedisException
    from klibee.exceptions.redis.no_metadata_in_redis     import NoMetadataInRedisException

    # .env
    from klibee.exceptions.env.no_variable                import NoVariableInEnvFileException

    # telegram
    from klibee.exceptions.telegram.cannot_connect_to_telegram  import CannotConnectTelegramException