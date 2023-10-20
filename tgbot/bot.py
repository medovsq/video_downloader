user_status = {}


if __name__ == "__main__":
    import aiogram
    import dispatcher
    import handlers
    
    # ping pseudo-unused imports
    handlers

    # start execution script
    aiogram.executor.start_polling(dispatcher.dp, skip_updates=True)
