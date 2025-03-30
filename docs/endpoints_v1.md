
# Endpoints

- endpoint `/user/{user-id}`
   - GET
   - DELETE
   - UPDATE
      - payload {UserName, Gender, Height, Age}

- endpoint `/user`
   - POST
       - payload {UserName, Gender, Height, Age}
       - Will create new user.


- endpoint `/steps/{user-id}`
   - GET
      - payload {StartDt, EndDt}
   - POST
       - payload {StartDt, EndDt, Steps}
       - Will create new steps entry.

- endpoint `/weights/{user-id}`
   - GET
      - payload {StartDt, EndDt}
   - DELETE
      - payload {Dt}
      - Deletes the weight entry of the Dt
   - POST
       - payload {Dt, Weight}
       - Will create new weight entry.

- endpoint `/reports/`
    - GET
       - Decision will be made once we finalize the AI/ML details.
