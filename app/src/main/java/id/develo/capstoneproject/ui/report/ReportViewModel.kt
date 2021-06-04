package id.develo.capstoneproject.ui.report

import android.util.Log
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import id.develo.capstoneproject.data.local.entity.ReportEntity
import id.develo.capstoneproject.data.remote.api.ApiConfig
import id.develo.capstoneproject.data.remote.response.ReportResponse
import id.develo.capstoneproject.ui.authentication.LoginViewModel
import id.develo.capstoneproject.utils.AppPreferences
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class ReportViewModel: ViewModel() {

    companion object {
        const val TAG = "ReportViewModel"
    }

    private var _isLoading = MutableLiveData<Boolean>()
    val isLoading: LiveData<Boolean> = _isLoading

    private var _isSuccess = MutableLiveData<Boolean>()
    val isSuccess: LiveData<Boolean> = _isSuccess

    private var _listReport = MutableLiveData<List<ReportEntity>>()
    val listReport: LiveData<List<ReportEntity>> = _listReport

    init {
        getReportData(AppPreferences.deviceId)
    }

    fun getReportData(deviceId: Int) {
        _isLoading.value = true

        val client = ApiConfig.getApiService().getReport(deviceId)
        client.enqueue(object : Callback<ReportResponse> {
            override fun onResponse(
                call: Call<ReportResponse>,
                response: Response<ReportResponse>
            ) {
                _isLoading.value = false
                if (response.isSuccessful) {
                    if (response.body()?.status == "OK") {
                        _isSuccess.value = true
                        _listReport.value = response.body()?.dataInfo
                    } else {
                        _isSuccess.value = false
                    }
                } else {
                    _isSuccess.value = false
                    Log.e(TAG, "GAGAL: ${response.message()}")
                }
            }

            override fun onFailure(call: Call<ReportResponse>, t: Throwable) {
                _isSuccess.value = false
                Log.e(TAG, "GAGAL: ${t.message.toString()}")
            }
        })
    }
}