Models
======

The app comes with the following models::


    UserDetails
        user
        email
        picture
        linkedin
        behance
        twitter
        instagram
        facebook
        youtube
        description
        education
        date_joined


    SupplierProfile
        user
        skills
        finished_connections_count
        connections_ranking_accumulator
        date_joined


    ConsumerProfile
        user
        date_joined

    
    Connection
        status
        supplier
        consumer 
        date_created
        date_finished
        objective
        rejection_reason
        finish_reason
        consumer_request_comments
        ranking
