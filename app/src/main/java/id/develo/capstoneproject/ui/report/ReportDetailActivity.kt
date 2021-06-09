package id.develo.capstoneproject.ui.report

import android.R.attr.name
import android.annotation.SuppressLint
import android.content.Intent
import android.net.Uri
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.bumptech.glide.Glide
import id.develo.capstoneproject.data.local.entity.ReportEntity
import id.develo.capstoneproject.databinding.ActivityReportDetailBinding


class ReportDetailActivity : AppCompatActivity() {

    companion object {
        const val EXTRA_REPORT = "extra_report"
    }

    private lateinit var binding: ActivityReportDetailBinding

    @SuppressLint("SetTextI18n")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityReportDetailBinding.inflate(layoutInflater)
        setContentView(binding.root)

        actionBar?.title = "Report Detail"
        actionBar?.setDisplayHomeAsUpEnabled(true)

        val reportDetail = intent.getParcelableExtra<ReportEntity>(EXTRA_REPORT)

        binding.tvCategory.text = reportDetail?.holeType
        binding.tvCoordinate.text = "${reportDetail?.latitude} | ${reportDetail?.longitude}"

        Glide.with(this)
            .load("https://storage.googleapis.com/pothole-detection1/" + reportDetail?.urlImg)
            .into(binding.imgResult)

        binding.btnMaps.setOnClickListener{
            val intent = Intent(Intent.ACTION_VIEW, Uri.parse("geo:0,0?q=${reportDetail?.latitude},${reportDetail?.longitude} (" + name + ")"))
            startActivity(intent)
        }
    }

    override fun onSupportNavigateUp(): Boolean {
        onBackPressed()
        return true
    }

    override fun onBackPressed() {
        super.onBackPressed()
        finish()
    }
}