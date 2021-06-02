package id.develo.capstoneproject.utils

import android.app.Application

class PotHoleApp : Application() {

    override fun onCreate() {
        super.onCreate()
        AppPreferences.init(this)
    }
}