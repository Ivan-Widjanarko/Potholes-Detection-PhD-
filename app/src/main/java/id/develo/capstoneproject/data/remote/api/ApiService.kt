package id.develo.capstoneproject.data.remote.api

import id.develo.capstoneproject.data.remote.response.GetUserResponse
import id.develo.capstoneproject.data.remote.response.PostUserResponse
import retrofit2.Call
import retrofit2.http.*

interface ApiService {

    @GET("user/login/{email}/{password}")
    fun userLogin(
        @Path("email") email: String,
        @Path("password") password: String
    ): Call<GetUserResponse>

    //    @FormUrlEncoded
    @POST("user/register/{email}/{password}/{device_id}/{state}")
    fun userRegister(
        @Path(encoded = false, value = "email") email: String,
        @Path("password") password: String,
        @Path("device_id") deviceId: Int,
        @Path("state") state: Int = 0
    ): Call<PostUserResponse>

}