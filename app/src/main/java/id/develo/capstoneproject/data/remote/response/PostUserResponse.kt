package id.develo.capstoneproject.data.remote.response

import com.google.gson.annotations.SerializedName

data class PostUserResponse (
    @field:SerializedName("message")
    val message: String?,

    @field:SerializedName("status")
    val status: String?
)