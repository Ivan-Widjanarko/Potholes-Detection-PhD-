package id.develo.capstoneproject.data.local.entity

import com.google.gson.annotations.SerializedName

data class UserEntity(

    @field:SerializedName("password")
    val password: String,

    @field:SerializedName("device_id")
    val deviceId: Int,

    @field:SerializedName("id")
    val id: Int,

    @field:SerializedName("email")
    val email: String
)
