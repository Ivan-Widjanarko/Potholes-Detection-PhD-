package id.develo.capstoneproject.data.remote.response

import com.google.gson.annotations.SerializedName
import id.develo.capstoneproject.data.local.entity.UserEntity

data class GetUserResponse(

	@field:SerializedName("user_info")
	val userInfo: UserEntity,

	@field:SerializedName("message")
	val message: String,

	@field:SerializedName("status")
	val status: String
)


