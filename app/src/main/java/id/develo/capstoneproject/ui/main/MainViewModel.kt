package id.develo.capstoneproject.ui.main

import android.util.Log
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import id.develo.capstoneproject.data.remote.api.ApiConfig
import id.develo.capstoneproject.data.remote.response.PostStatusResponse
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class MainViewModel: ViewModel() {

    companion object {
        const val TAG = "MainViewModel"
    }

    private var _isLoading = MutableLiveData<Boolean>()
    val isLoading: LiveData<Boolean> = _isLoading

    private var _isSuccess = MutableLiveData<Boolean>()
    val isSuccess: LiveData<Boolean> = _isSuccess

    fun setState(id: Int, state: Int) {
        _isLoading.value = true

        val client = ApiConfig.getApiService().setUserState(id, state)
        client.enqueue(object : Callback<PostStatusResponse> {
            override fun onResponse(
                call: Call<PostStatusResponse>,
                response: Response<PostStatusResponse>
            ) {
                _isLoading.value = false
                if (response.isSuccessful) {
                    _isSuccess.value = response.body()?.status == "OK"

                } else {
                    _isSuccess.value = false
                    Log.e(TAG, "GAGAL: ${response.message()}")
                }
            }

            override fun onFailure(call: Call<PostStatusResponse>, t: Throwable) {
                _isSuccess.value = false
                _isLoading.value = false
                Log.e(TAG, "onFailure: ${t.message.toString()}")
            }
        })
    }
}