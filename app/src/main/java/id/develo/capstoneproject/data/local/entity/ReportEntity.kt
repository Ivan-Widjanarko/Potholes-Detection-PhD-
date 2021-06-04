package id.develo.capstoneproject.data.local.entity

import com.google.gson.annotations.SerializedName

data class ReportEntity(

    @field:SerializedName("hole_type")
    val holeType: String,

    @field:SerializedName("url_img")
    val urlImg: String,

    @field:SerializedName("device_id")
    val deviceId: Int,

    @field:SerializedName("latitude")
    val latitude: Double,

    @field:SerializedName("id")
    val id: Int,

    @field:SerializedName("longitude")
    val longitude: Double
)