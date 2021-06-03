package id.develo.capstoneproject.ui.main

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.Menu
import android.view.MenuInflater
import android.view.MenuItem
import android.view.View
import androidx.activity.viewModels
import com.bumptech.glide.Glide
import com.google.android.material.snackbar.Snackbar
import id.develo.capstoneproject.R
import id.develo.capstoneproject.databinding.ActivityMainBinding
import id.develo.capstoneproject.ui.about.AboutActivity
import id.develo.capstoneproject.ui.authentication.AuthActivity
import id.develo.capstoneproject.utils.AppPreferences

class MainActivity : AppCompatActivity() {

    companion object {
        const val SNACKBAR_TEXT = "snackbar_text"
        const val IS_LOGGED_IN = "is_logged_in"
    }

    private lateinit var binding: ActivityMainBinding
    private val mainViewModel: MainDrivingViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // Launch a snackbar from login page
        if (intent.getBooleanExtra(IS_LOGGED_IN, false)) {
            onSnack()
        }

        // Set progress bar if start button is clicked.
        setProgressBar()

        moveToAbout()

        mainViewModel.isSuccess.observe(this, {
            if (it) {
                Intent(this, DrivingActivity::class.java).also { intent ->
                    startActivity(intent)
                }
            }
        })

        binding.btnStart.setOnClickListener {
            if (AppPreferences.isLogin) {
                mainViewModel.setState(AppPreferences.uId, 1)
            }

        }

        Glide.with(this)
            .load(R.drawable.img_banner)
            .into(binding.imageView)
    }

    private fun onSnack() {
        Snackbar.make(
            this@MainActivity.window.decorView.rootView,
            intent.getStringExtra(SNACKBAR_TEXT).toString(),
            Snackbar.LENGTH_SHORT
        ).show()
    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        val inflater: MenuInflater = menuInflater
        inflater.inflate(R.menu.main_menu, menu)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        // Handle item selection
        return when (item.itemId) {
            R.id.action_logout -> {
                logout()
                true
            }
            else -> super.onOptionsItemSelected(item)
        }
    }

    private fun setProgressBar() {
        mainViewModel.isLoading.observe(this, {
            binding.progressBar.visibility = if (it) View.VISIBLE else View.GONE
        })
    }

    private fun logout() {
        if (AppPreferences.isLogin) {
            AppPreferences.isLogin = false
            AppPreferences.uId = 0
            AppPreferences.email = ""
            AppPreferences.password = ""
        }
        Intent(this, AuthActivity::class.java).also {
            startActivity(it)
            finish()
        }
    }

    private fun moveToAbout() {
        binding.btnAbout.setOnClickListener {
            Intent(this, AboutActivity::class.java).also {
                startActivity(it)
            }
        }
    }
}