package id.develo.capstoneproject.data.remote.response

import com.google.gson.annotations.SerializedName
import id.develo.capstoneproject.data.local.entity.ReportEntity

data class ReportResponse(

	@field:SerializedName("data_info")
	val dataInfo: List<ReportEntity>,

	@field:SerializedName("message")
	val message: String,

	@field:SerializedName("status")
	val status: String
)


