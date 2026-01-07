def retrieve(store, backstory, k=6):
    return store.retrieve_query(
        queries=[backstory],
        k=k
    )

