## Fast API related:
- When you declare a path operation function with normal def instead of async def, it is run in an external threadpool that is then awaited, 
instead of being called directly (as it would block the server).
- If a dependency is a standard def function instead of async def, it is run in the external threadpool.
- It's "concurrent safe" as long as we use local variables.

## Async related:
- Writing to db:
   - Sync case: db acknowledges db write was successful, so the thread was blocked till then.
   - Async case: Thread raising the write request is not blocked. Write request is added to a queue and written later. Thread raising the request sees its written but its not.
   Durability is lost. ACI is maintained.
- Reading is immune.

## References:
- https://fastapi.tiangolo.com/async/#very-technical-details
- https://github.com/fastapi/fastapi/issues/2619
- https://sqlite.org/asyncvfs.html
- https://www.postgresql.org/docs/current/wal-async-commit.html