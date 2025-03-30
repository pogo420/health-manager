# Db plan v1

- There will be three tables:
   - User(UserId, UserName, Gender, Height, Age)
   - Steps(UserId, StartDt, EndDt, Steps)
   - Weight(UserId, Dt, Weight)

- Start with sqlite, will migrate if required.
- Repository pattern will be followed.